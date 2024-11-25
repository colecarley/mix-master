from sqlalchemy import Column, DateTime, ForeignKey, Integer, Sequence, String, VARCHAR
from database import Base

class Mix(Base):
    __tablename__ = "mixes"
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("projects.id"), primary_key=True)
    created_at = Column(DateTime, primary_key=True)
    description = Column(VARCHAR(255))
    name = Column(VARCHAR(255))

    