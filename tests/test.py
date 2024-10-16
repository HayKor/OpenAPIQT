from swaggerqt.models import (
    Components,
    ExternalDocs,
    Info,
    MediaType,
    OpenAPI,
    Operation,
    Path,
    RequestBody,
    Response,
    Schema,
    Server,
    Tag,
)


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
                            "application/json": MediaType(
                                schema_field=Schema(
                                    type="array",
                                    items=Schema(type="object"),
                                )
                            )
                        },
                    )
                },
            ),
            post=Operation(
                tags=["users"],
                summary="Create a new user",
                description="Create a new user",
                requestBody=RequestBody(
                    description="User  data",
                    content={
                        "application/json": MediaType(
                            schema_field=Schema(
                                type="object",
                                properties={
                                    "name": Schema(type="string"),
                                    "email": Schema(type="string"),
                                },
                            )
                        )
                    },
                ),
                responses={
                    "201": Response(
                        description="User  created",
                        content={
                            "application/json": MediaType(
                                schema_field=Schema(
                                    type="object",
                                    properties={
                                        "id": Schema(type="integer"),
                                        "name": Schema(type="string"),
                                        "email": Schema(type="string"),
                                    },
                                )
                            )
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
                            "application/json": MediaType(
                                schema_field=Schema(
                                    type="array", items=Schema(type="object")
                                )
                            )
                        },
                    )
                },
            )
        ),
    },
    components=Components(
        schemas={
            "User ": Schema(
                type="object",
                properties={
                    "id": Schema(type="integer"),
                    "name": Schema(type="string"),
                    "email": Schema(type="string"),
                },
            ),
            "Product": Schema(
                type="object",
                properties={
                    "id": Schema(type="integer"),
                    "name": Schema(type="string"),
                    "price": Schema(type="number"),
                },
            ),
        },
        responses={
            "Error": Response(
                description="Error response",
                content={
                    "application/json": MediaType(
                        schema_field=Schema(
                            type="object",
                            properties={"message": Schema(type="string")},
                        )
                    )
                },
            )
        },
        requestBodies={
            "User": RequestBody(
                description="User  data",
                content={
                    "application/json": MediaType(
                        schema_field=Schema(
                            type="object",
                            properties={
                                "name": Schema(type="string"),
                                "email": Schema(type="string"),
                            },
                        )
                    )
                },
            )
        },
    ),
)


def test_openapi_complex():
    assert openapi.info.title == "My API"
    assert openapi.info.version == "1.0.0"
    assert openapi.info.description == "This is my API"

    assert len(openapi.servers) == 2
    assert openapi.servers[0].url == "https://api.example.com"
    assert openapi.servers[0].description == "Production Server"

    assert len(openapi.tags) == 2
    assert openapi.tags[0].name == "users"
    assert openapi.tags[0].description == "Operations related to users"

    assert "/users" in openapi.paths
    assert openapi.paths["/users"].get.tags == ["users"]
    assert openapi.paths["/users"].get.summary == "Get all users"
    assert (
        openapi.paths["/users"].get.responses["200"].description == "Users list"
    )

    assert (
        openapi.paths["/users"]
        .post.requestBody.content["application/json"]
        .schema_field.type
        == "object"
    )
    assert (
        openapi.paths["/users"]
        .post.responses["201"]
        .content["application/json"]
        .schema_field.type
        == "object"
    )

    assert "/products" in openapi.paths
    assert openapi.paths["/products"].get.tags == ["products"]
    assert openapi.paths["/products"].get.summary == "Get all products"


if __name__ == "__main__":
    test_openapi_complex()
