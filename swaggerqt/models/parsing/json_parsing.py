import logging
from typing import Any, Type

from pydantic import BaseModel, Field, RootModel, create_model
from pydantic.json_schema import GenerateJsonSchema


class SkipDefs(GenerateJsonSchema):
    def generate(self, schema, mode="validation"):
        json_schema = super().generate(schema, mode=mode)
        if "$defs" in json_schema:
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
        logging.debug("JsonParser has initialized")

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

            if prop in jschema.get("required", []):
                default_value = ...
            else:
                default_value = schema.get("default", None)
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

        # Register the model
        self._type_dict[model_name] = model
        logging.debug(f"Saved model with name {model_name}")

        return model

    def get_all_types_dict(self) -> dict[str, Type]:
        return self._type_dict

    def get_all_types_list(self) -> list[str]:
        # TODO: actually implement logic for `array` (array of what?)
        types_list = list(self._type_dict.keys())

        # For now
        types_list.remove("array")
        return types_list

    def get_json_schema(
        self, model_name: str, pop_title: bool = True
    ) -> dict[str, Any]:
        """Return empty dict when error occurs"""
        try:
            model = self._type_dict[model_name]
            if issubclass(model, BaseModel) or issubclass(model, RootModel):
                schema = model.model_json_schema(
                    ref_template="#/components/schemas/{model}",
                    schema_generator=SkipDefs,
                )
            else:
                root_model = RootModel[model]
                schema = root_model.model_json_schema(
                    ref_template="#/components/schemas/{model}"
                )
            if pop_title:
                schema.pop("title")
            return schema

        except KeyError as e:
            logging.error(
                "Couldn't get model with name %s, error: %q", model_name, e
            )

        except Exception as e:
            logging.error(
                "Something unexpected when processing model_name %s, error: %q",
                model_name,
                e,
            )

        return {}
