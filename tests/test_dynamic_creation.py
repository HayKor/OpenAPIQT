import json
from typing import Any, Optional

from pydantic import BaseModel, Field, create_model
from pydantic.json_schema import GenerateJsonSchema


"""
DynamicModel = create_model(
    'DynamicModel',
    foo=(str, Field(..., description='foo description', alias='FOO')),
)
"""

type_dict: dict[str, type] = {
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


def generate_dynamic_model(
    model_name: str, jschema: dict[str, Any]
) -> type[BaseModel]:
    fields = {}

    if jschema.get("type") != "object":
        pass

    for prop, schema in jschema["properties"].items():
        prop_type: type | Any = type_dict.get(schema["type"], Any)
        if prop_type == list:
            prop_type = list[schema.get("items", Any)]

        default_value = ...
        example = None

        if not prop in jschema.get("required", []):
            prop_type = Optional[prop_type]
            default_value = None

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
    type_dict[model.__name__] = model

    return model


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
    ],
}

User = generate_dynamic_model("User", user_schema)

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

ArrayOfUsers = generate_dynamic_model("ArrayOfUsers", array_of_users_schema)

print(
    json.dumps(
        ArrayOfUsers.model_json_schema(
            ref_template="#/components/schemas/{model}",
            schema_generator=SkipDefs,
        ),
        indent=2,
    )
)
