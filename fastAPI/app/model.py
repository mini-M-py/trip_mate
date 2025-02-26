from .database import Base
from sqlalchemy import ARRAY, Text, Column, Integer, String, Boolean, ForeignKey, false
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import Relationship, relationship

class Visitor(Base):
    __tablename__ = "visitor"
    id = Column(Integer, primary_key=True, nullable=False)
    user_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default = text('now()'))
    gender =  Column(String, nullable=False)
    country = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    profile_pic =Column(String, nullable=False)

class Guide(Base):
    __tablename__ = "guide"
    id = Column(Integer, primary_key=True, nullable=False)
    user_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default = text('now()'))
    gender =  Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    country = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    biography = Column(Text)
    rating = Column(Integer, nullable=False, server_default='0')
    profile_pic = Column(String, nullable=False)
    languages = Column(ARRAY(String), nullable=False)
    specialization = Column(String, nullable=False)
    availability = Column(String, nullable=False)
    additional_skills = Column(ARRAY(String), nullable=False)
    tours_no = Column(Integer, server_default= '0')
    payment_methods = Column(ARRAY(String), nullable=False)
    is_booked = Column(Boolean, server_default='False')


class Plan(Base):
    __tablename__ = "trip_plan"
    id = Column(Integer, primary_key=True, nullable=False) 
    guide_id = Column(Integer, ForeignKey("guide.id", ondelete='CASCADE'), nullable=False) 
    title = Column(String, nullable=False)
    discription = Column(Text, nullable=False)
    tour_type = Column(String, nullable=False, server_default="private")
    transportation  = Column(String, nullable=False)
    reviews_count = Column(Integer, nullable=False, server_default="0")
    price = Column(Integer, nullable=False)
    owner = relationship('Guide')






