from typing import Any, Type

from pydantic import BaseModel, Field, create_model
from pydantic.json_schema import GenerateJsonSchema


class SkipDefs(GenerateJsonSchema):
    def generate(self, schema, mode="validation"):
        json_schema = super().generate(schema, mode=mode)
        json_schema.pop("$defs")
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
        prop_type = self._type_dict.get(jschema.get("type", Any))

        if isinstance(prop_type, list):
            prop_type = list[
                self._type_dict.get(jschema.get("items", Any), Any)
            ]

        return prop_type

    def parse_json_schema(
        self, model_name: str, jschema: dict[str, Any]
    ) -> BaseModel | Any:
        """
        Parse JSON schema and return `pydantic.BaseModel` or `type` (ref to `self.parses_type()`).
        """

        fields = {}

        if jschema.get("type", Any) != "object":
            prop_type = self.parse_type(jschema)
            return prop_type

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

        # TODO: save to DB or smth

        # Register the model
        self._type_dict[model_name] = model

        return model
