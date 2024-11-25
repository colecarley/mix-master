from sqlalchemy import Column, Integer, Sequence, String, VARCHAR
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    username = Column(VARCHAR(255), primary_key=True, index=True)
    password = Column(VARCHAR(255))
    first_name = Column(VARCHAR(255))
    last_name = Column(VARCHAR(255))
    