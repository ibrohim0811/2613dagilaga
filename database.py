from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
# from main import DATABASE_URL

DATABASE_URL = "sqlite:///./ijarachi.db"
print(DATABASE_URL)

engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()