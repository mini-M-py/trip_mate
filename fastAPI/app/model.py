from .database import Base
from sqlalchemy import ARRAY, Text, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import Relationship

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
    group_size = Column(String, nullable=False)
    additional_skills = Column(ARRAY(String), nullable=False)
    tour_types = Column(String, nullable=False)
    tours_no = Column(Integer, server_default= '0')
    transportation = Column(String, nullable=False)
    area_covered  = Column(ARRAY(String), nullable=False)
    payment_methods = Column(ARRAY(String), nullable=False)
    is_booked = Column(Boolean, server_default='False')












