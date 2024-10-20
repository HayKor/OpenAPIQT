import logging
from typing import Any, Type

from pydantic import BaseModel, Field, RootModel, create_model
from pydantic.json_schema import GenerateJsonSchema


class SkipDefs(GenerateJsonSchema):
    def generate(self, schema, mode="validation"):
        json_schema = super().generate(schema, mode=mode)
        json_schema.pop("$defs")
        return json_schema


class RemoveTitle(GenerateJsonSchema):
    def generate(self, schema, mode="validation"):
        json_schema = super().generate(schema, mode=mode)
        json_schema.pop("title")
        return json_schema


class JsonParser:
    """
    Class for parsing JSON either into `type` or into `type[pydantic.BaseModel]`
    """

    def __init__(self) -> None:
        self._type_dict: dict[str, Type] = {
            "string": str,
            "integer": int,
            "number": float,
            "boolean": bool,
            "array": list,
        }

    def parse_type(
        self,
        jschema: dict[str, Any],
    ) -> int | str | bool | float | list[object] | Any:
        """
        Parse single type and return it.
        If not found, returns `Any`
        """

        prop_type = self._type_dict.get(jschema.get("type", Any), Any)

        logging.debug("Parsed type of prop_type=%s", prop_type)

        if prop_type == list:
            items_type = self._type_dict.get(jschema["items"].get("type", Any))
            prop_type = list[items_type]

            logging.debug("Parsed list type of prop_type=%s", prop_type)

        return prop_type

    def parse_json_schema(
        self, model_name: str, jschema: dict[str, Any]
    ) -> type[BaseModel] | type[RootModel]:
        """
        Parse JSON schema and return `pydantic.BaseModel` or `RootModel[type]` (ref to `self.parses_type()`).
        """

        fields = {}

        if jschema.get("type", Any) != "object":
            prop_type = self.parse_type(jschema)
            logging.info(
                "Created RootModel of %s with name %s",
                prop_type,
                model_name,
            )

            model = RootModel[prop_type]
            model.__name__ = model_name
            return model

        for prop, schema in jschema.get("properties", {}).items():
            prop_type = self.parse_type(schema)

            default_value = schema.get("default", ...)
            examples = schema.get("examples", None)

            fields[prop] = (
                prop_type,
                Field(
                    default_value,
                    examples=examples,
                ),
            )

        model = create_model(model_name, **fields)
        logging.info(
            "Created BaseModel with name %s and fields %s",
            model_name,
            fields.keys(),
        )

        # TODO: save to DB or smth

        # Register the model
        self._type_dict[model_name] = model
        logging.debug(f"Saved model with name {model_name}")

        return model
