from sqlalchemy import Column, DateTime, Integer, ForeignKey, Date, VARCHAR
from database import Base

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    created_at = Column(DateTime, primary_key=True)
    description = Column(VARCHAR(255))
    name = Column(VARCHAR(255))
    start_date = Column(Date)
    end_date = Column(Date)



