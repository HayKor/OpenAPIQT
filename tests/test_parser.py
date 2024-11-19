import json

from swaggerqt.models.parsing import JsonParser


def test_parser():
    parser = JsonParser()

    assert (
        parser.parse_type({"type": "array", "items": {"type": "string"}})
        == list[str]
    )

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
    User = parser.parse_json_schema("User", user_schema)
    user_array_schema = {
        "type": "array",
        "items": {
            "type": "User",
        },
    }
    assert parser.parse_type(user_array_schema) == list[User]

    assert User.model_json_schema(
        ref_template="#/components/schemas/{model}"
    ) == parser.get_json_schema("User", pop_title=False)
