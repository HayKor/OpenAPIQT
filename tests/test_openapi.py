import json

import yaml

from swaggerqt.models import (
    Components,
    ExternalDocs,
    Info,
    OpenAPI,
    Operation,
    Path,
    RequestBody,
    Response,
    Server,
    Tag,
)
from tests.test_dynamic_creation import parse_json_schema


openapi = OpenAPI(
    openapi="3.0.0",
    info=Info(title="My API", version="1.0.0", description="This is my API"),
    externalDocs=ExternalDocs(
        url="https://example.com/docs", description="API Documentation"
    ),
    servers=[
        Server(url="https://api.example.com", description="Production Server"),
        Server(
            url="https://staging.api.example.com", description="Staging Server"
        ),
    ],
    tags=[
        Tag(
            name="users",
            description="Operations related to users",
            externalDocs=ExternalDocs(
                url="https://example.com/docs/users",
                description="User  Documentation",
            ),
        ),
        Tag(name="products", description="Operations related to products"),
    ],
    paths={
        "/users": Path(
            get=Operation(
                tags=["users"],
                summary="Get all users",
                description="Retrieve a list of all users",
                responses={
                    "200": Response(
                        description="Users list",
                        content={
                            "application/json": {}
                            # parse_json_schema(
                            #     "TestModel",
                            #     {
                            #         "type": "array",
                            #         "items": "User",
                            #     },
                            # )
                        },
                    )
                },
            ),
            post=Operation(
                tags=["users"],
                summary="Create a new user",
                description="Create a new user",
                requestBody=RequestBody(
                    description="User data",
                    content={
                        "application/json": {
                            "schema": parse_json_schema(
                                "User",
                                {
                                    "type": "object",
                                    "properties": {
                                        "name": {
                                            "type": "string",
                                        },
                                        "email": {
                                            "type": "string",
                                        },
                                    },
                                },
                            ).model_json_schema()
                        }
                    },
                ),
                responses={
                    "201": Response(
                        description="User  created",
                        content={
                            "application/json": {
                                "schema": parse_json_schema(
                                    "User",
                                    {
                                        "type": "object",
                                        "properties": {
                                            "id": {
                                                "type": "integer",
                                            },
                                            "name": {
                                                "type": "string",
                                            },
                                            "email": {
                                                "type": "string",
                                            },
                                        },
                                    },
                                ).model_json_schema()
                            }
                        },
                    )
                },
            ),
        ),
        "/products": Path(
            get=Operation(
                tags=["products"],
                summary="Get all products",
                description="Retrieve a list of all products",
                responses={
                    "200": Response(
                        description="Products list",
                        content={
                            "application/json": {
                                "schema": parse_json_schema(
                                    "Product",
                                    {
                                        "type": "object",
                                        "properties": {
                                            "id": {
                                                "type": "string",
                                            },
                                            "name": {
                                                "type": "string",
                                            },
                                            "price": {
                                                "type": "integer",
                                            },
                                        },
                                    },
                                ).model_json_schema()
                            }
                        },
                    )
                },
            )
        ),
    },
    components=Components(
        schemas={
            "User": parse_json_schema(
                "User",
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer",
                        },
                        "name": {
                            "type": "string",
                        },
                        "email": {
                            "type": "string",
                        },
                    },
                },
            ).model_json_schema(),
            "Product": parse_json_schema(
                "Product",
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string",
                        },
                        "name": {
                            "type": "string",
                        },
                        "price": {
                            "type": "integer",
                        },
                    },
                },
            ).model_json_schema(),
        },
        responses={
            "Error": Response(
                description="Error response",
                content={
                    "application/json": {
                        "schema": parse_json_schema(
                            "Error",
                            {
                                "type": "object",
                                "properties": {
                                    "message": {
                                        "type": "string",
                                    },
                                },
                            },
                        ).model_json_schema()
                    }
                },
            )
        },
        requestBodies={
            "User": RequestBody(
                description="User data",
                content={
                    "application/json": {
                        "schema": parse_json_schema(
                            "User",
                            {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "integer",
                                    },
                                    "name": {
                                        "type": "string",
                                    },
                                    "email": {
                                        "type": "string",
                                    },
                                },
                            },
                        ).model_json_schema()
                    }
                },
            )
        },
    ),
)


def test_openapi_complex():
    pass


if __name__ == "__main__":
    #
    # print(
    #     openapi.model_dump_json(
    #         exclude_none=True,
    #         exclude_unset=True,
    #     )
    # )

    print(
        yaml.safe_dump(
            openapi.model_dump(
                exclude_none=True,
                exclude_unset=True,
                exclude_defaults=True,
            ),
            indent=2,
            sort_keys=False,
        )
    )

    # print(
    #     json.dumps(
    #         openapi.model_dump(
    #             exclude_none=True,
    #             exclude_unset=True,
    #         ),
    #         indent=2,
    #     )
    # )
    #
    test_openapi_complex()
