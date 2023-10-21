from typing import Union

from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engin
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

def create_async_engin(url: Union[URL, str]) -> AsyncEngine:
    return _create_async_engin(url=url, echo=True, pool_pre_ping=True)

async def proceeed_schemas(engine: AsyncEngine, metadata) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

def get_session_maker(engine: AsyncEngine) -> sessionmaker:
    return sessionmaker(engine, class_=AsyncSession)