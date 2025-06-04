from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from database import create_tables

from api.v1.router import router



@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/shop-verification-oa2QMqN2Al.txt", response_class=PlainTextResponse)
async def verification_file():
    return "shop-verification-oa2QMqN2Al"

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)