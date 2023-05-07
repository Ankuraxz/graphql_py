import typing
import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL


# Data Structure
@strawberry.type
class User:
    name: str
    age: int
    addresses: list["Address"]



@strawberry.type
class Address:
    person: User
    street: str
    city: str
    state: str
    zip_code: str


def get_user(self) -> typing.List[User]:
    address = Address(person=None, street="123 Main St", city="Anytown", state="CA", zip_code="12345")
    user = User(name="John", age=30, addresses=[address])
    address.person = user
    return [user]


@strawberry.type
class Query:
    users: typing.List[User] = strawberry.field(resolver=get_user)


schema = strawberry.Schema(query=Query)

# Create a FastAPI app
app = FastAPI()

# Define multiple routes for the app
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Mount the GraphQL app on a route
app.add_route("/graphql", GraphQL(schema))

# Add a WebSocket route for the GraphQL endpoint
app.add_websocket_route("/graphql", GraphQL(schema))






