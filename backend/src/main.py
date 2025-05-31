from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from database import create_tables

from api.v1.router import router



@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)

@app.post("/")
async def debug(request: Request):
    print("🔥 Новый запрос получен")

    # query-параметры
    query_params = dict(request.query_params)
    print("🧩 Query parameters:", query_params)

    content_type = request.headers.get("content-type", "")
    print("📃 Content-Type:", content_type)

    body_data = None

    if "application/json" in content_type:
        try:
            body_data = await request.json()
            print("📦 JSON тело:", body_data)
        except Exception as e:
            print("⚠️ Ошибка JSON:", e)

    elif "application/x-www-form-urlencoded" in content_type:
        try:
            form = await request.form()
            body_data = dict(form)
            print("📝 Form data:", body_data)
        except Exception as e:
            print("⚠️ Ошибка формы:", e)

    else:
        print("❓ Неизвестный формат тела запроса")

    return {
        "query_params": query_params,
        "body": body_data
    }


origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)