from sqlalchemy import Column, DateTime, ForeignKey, Integer
from database import Base

class Proportion(Base):
    __tablename__ = "proportions"
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    mix_id = Column(Integer, ForeignKey("mixes.id"), primary_key=True)
    material_id = Column(Integer, ForeignKey("materials.id"), primary_key=True)  
    quantity = Column(Integer)
    unit_id = Column(Integer, ForeignKey("units.id"))


    