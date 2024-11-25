from sqlalchemy import Column, ForeignKey, Integer, VARCHAR
from database import Base

class Material(Base):
    __tablename__ = "materials"
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    mix_id = Column(Integer, ForeignKey("mixes.id"), primary_key=True) 
    name = Column(VARCHAR(255), primary_key=True)
    cost_per_unit = Column(Integer)
    unit_id = Column(Integer, ForeignKey("units.id"))


    