from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from dotenv import load_dotenv

from app.database import Base, SessionLocal, engine, migrate_schema
from app.routers import api, web
from app.seed import seed_if_empty

load_dotenv()


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    migrate_schema()
    db = SessionLocal()
    try:
        seed_if_empty(db)
    finally:
        db.close()
    yield


app = FastAPI(
    title="UniShare Makerspace",
    description="Institutional makerspace and lab equipment sharing platform.",
    version="1.0.0",
    lifespan=lifespan,
)

static_dir = Path(__file__).resolve().parent / "static"
static_dir.mkdir(exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")
app.include_router(web.router)
app.include_router(api.router)
