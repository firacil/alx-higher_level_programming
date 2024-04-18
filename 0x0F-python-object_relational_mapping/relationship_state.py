#!/usr/bin/python3
"""
python file contains class definition
of a state and an instance Base
"""

from sqlalchemy import Column,  Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
        class state inherting from Base
        State will be my database table
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
