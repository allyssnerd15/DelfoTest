from os import getenv

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql+asyncpg://admin:admin@localhost:5432/delfo'


engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(engine, class_=AsyncSession)