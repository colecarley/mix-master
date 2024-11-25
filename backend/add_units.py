from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import pandas as pd;
import entities.unit as Unit

DATABASE_URL = "postgresql+psycopg2://postgres:password@localhost:5433/postgres"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_units():
    path = "/Users/colecarley/src/mix-master/backend/migrations/clean-units-of-measure.csv"
    df = pd.read_csv(path)
    return df

df = get_units()



for (i, row) in df.iterrows():
    unit = Unit.Unit(name=row["Name"], symbol=row["Symbol"])
    gen = get_db()
    db = next(gen)
    db.add(unit)
    db.commit()
    db.refresh(unit)
