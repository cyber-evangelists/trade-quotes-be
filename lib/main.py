from types import SimpleNamespace

from beanie import init_beanie
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, Response
import strawberry
from strawberry.asgi import GraphQL

from lib import config
from lib.models.entities.seller_entity import SellerEntity
from lib.models.entities.seller_tag_entity import SellerTagEntity
from lib.models.entities.user_entity import UserEntity
from lib.models.types.query import Query
from lib.models.types.mutation import Mutation
from lib.services import jwt


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQL(schema)

app = FastAPI()


@app.on_event('startup')
async def start():
    await init_beanie(
        connection_string=f'mongodb://root:abcdefgh@{config.DB_HOST}/tradequotes?authSource=admin',
        document_models=[
            SellerEntity,
            SellerTagEntity,
            UserEntity,
        ],
    )
    if await SellerTagEntity.count() == 0:
        await SellerTagEntity.insert_many([
            SellerTagEntity(label='Pressure Washing'),
            SellerTagEntity(label='Roof Cleaning'),
            SellerTagEntity(label='Gutter Cleaning'),
        ])
    print('initialized beanie odm')


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware('http')
async def auth(request: Request, call_next):
    auth_header = request.headers.get('Authorization')
    try:
        if auth_header:
            token = auth_header[len('Bearer '):]
            decoded = jwt.decode(token)
            if decoded.get('userId'):
                request.state.auth_user = SimpleNamespace(
                    id=decoded.get('userId'))

        return await call_next(request)
    except:
        return Response(status_code=401)

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)
