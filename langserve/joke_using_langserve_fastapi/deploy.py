from fastapi import FastAPI
from langserve import add_routes
from test_app import chain

app = FastAPI()

add_routes(app, chain, path='/joke')
