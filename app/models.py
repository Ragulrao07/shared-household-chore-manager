from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    household_id = Column(Integer, ForeignKey("households.id"), nullable=True)
    
    household = relationship("Household", back_populates="members")

class Household(Base):
    __tablename__ = "households"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    invite_code = Column(String, unique=True, index=True)
    
    members = relationship("User", back_populates="household")
    chores = relationship("Chore", back_populates="household")

class Chore(Base):
    __tablename__ = "chores"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String, nullable=True)
    frequency = Column(String) # e.g., "weekly"
    due_date = Column(DateTime)
    household_id = Column(Integer, ForeignKey("households.id"))
    current_assignee_id = Column(Integer, ForeignKey("users.id"))
    is_deleted = Column(Boolean, default=False) # Soft delete as per plan
    
    household = relationship("Household", back_populates="chores")
    history = relationship("ChoreHistory", back_populates="chore")

class ChoreHistory(Base):
    __tablename__ = "chore_history"
    id = Column(Integer, primary_key=True, index=True)
    chore_id = Column(Integer, ForeignKey("chores.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    completed_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    chore = relationship("Chore", back_populates="history")
