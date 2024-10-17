import json
from typing import Any, Optional, Type

from pydantic import BaseModel, Field, create_model
from pydantic.json_schema import GenerateJsonSchema


TYPE_DICT: dict[str, Type] = {
    "string": str,
    "integer": int,
    "number": float,
    "boolean": bool,
    "array": list,
}


class SkipDefs(GenerateJsonSchema):
    def generate(self, schema, mode="validation"):
        json_schema = super().generate(schema, mode=mode)
        json_schema.pop("$defs")
        return json_schema


def parse_type(jschema: dict[str, Any]) -> Optional[Type[list | Any | object]]:
    prop_type = TYPE_DICT.get(jschema.get("type", Any))

    if prop_type == list:
        prop_type = list[TYPE_DICT.get(jschema.get("items", Any), Any)]

    return prop_type


def parse_json_schema(
    model_name: str, jschema: dict[str, Any]
) -> type[BaseModel] | Any:
    fields = {}

    if jschema.get("type") != "object":
        prop_type = parse_type(jschema)
        return prop_type

    for prop, schema in jschema["properties"].items():
        prop_type = parse_type(schema)

        default_value = ...
        example = None

        # if not prop in jschema.get("required", []):
        #     prop_type = Optional[prop_type]
        #     default_value = None

        if schema.get("example", None):
            example = schema.get("example")

        fields[prop] = (
            prop_type,
            Field(
                default_value,
                examples=example,
            ),
        )

    model = create_model(model_name, **fields)
    TYPE_DICT[model.__name__] = model

    return model


if __name__ == "__main__":
    assert parse_type({"type": "array", "items": "string"}) == list[str]
    user_schema = {
        "type": "object",
        "properties": {
            "id": {
                "title": "Id",
                "type": "integer",
            },
            "name": {
                "title": "Name",
                "type": "string",
                "example": "Arthur",
            },
            "age": {
                "title": "Age",
                "type": "integer",
            },
        },
        "required": [
            "id",
            "name",
            "age",
        ],
    }

    User = parse_json_schema("User", user_schema)

    array_of_users_schema = {
        "type": "object",
        "properties": {
            "users": {
                "type": "array",
                "items": "User",
            }
        },
        "required": "users",
    }

    ArrayOfUsers = parse_json_schema("ArrayOfUsers", array_of_users_schema)

    user_array = {
        "type": "array",
        "items": "User",
    }
    user_array = parse_json_schema("array", user_array)
    print(user_array)

    print(
        json.dumps(
            ArrayOfUsers.model_json_schema(
                ref_template="#/components/schemas/{model}",
                schema_generator=SkipDefs,
            ),
            indent=2,
        )
    )
