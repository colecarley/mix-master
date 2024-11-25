from sqlalchemy import Column, DateTime, ForeignKey, Integer, Sequence, String, VARCHAR, DECIMAL
from database import Base

class Unit(Base):
    __tablename__ = "units"
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    name = Column(VARCHAR(255), primary_key=True)
    symbol = Column(VARCHAR(50), primary_key=True)
    