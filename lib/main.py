import os
from beanie import init_beanie
import strawberry
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.asgi import GraphQL

from lib.graphql import Query, Mutation
from lib.models.entities.seller_entity import SellerEntity
from lib.models.entities.tag_entity import TagEntity
from lib.models.entities.user_entity import UserEntity


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQL(schema)

app = FastAPI()


@app.on_event('startup')
async def start():
    await init_beanie(
        connection_string=f'mongodb://root:abcdefgh@{os.environ["DB_HOST"]}/tradequotes?authSource=admin',
        document_models=[
            SellerEntity,
            TagEntity,
            UserEntity,
        ],
    )
    if await TagEntity.count() == 0:
        await TagEntity.insert_many([
            TagEntity(label='Pressure Washing'),
            TagEntity(label='Roof Cleaning'),
            TagEntity(label='Gutter Cleaning'),
        ])
    print('initialized beanie odm')


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)
