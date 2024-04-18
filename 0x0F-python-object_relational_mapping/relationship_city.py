#!/usr/bin/python3
"""
python file contains class definition
of a state and an instance Base
"""
from relationship_state import Base, State
from sqlalchemy import Column,  Integer, String, ForeignKey


class City(Base):
    """
        class city inherting from Base
        city will be my database table
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
