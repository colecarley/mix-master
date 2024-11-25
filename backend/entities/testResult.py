from sqlalchemy import Column, DateTime, ForeignKey, Integer, Sequence, String, VARCHAR, DECIMAL
from database import Base

class TestResult(Base):
    __tablename__ = "test_results"
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    mix_id = Column(Integer, ForeignKey("mixes.id"), primary_key=True)
    test_date = Column(DateTime, primary_key=True)
    property_measured = Column(VARCHAR(255), primary_key=True)
    result = Column(Integer)
    unit_id = Column(Integer, ForeignKey("units.id"))


    