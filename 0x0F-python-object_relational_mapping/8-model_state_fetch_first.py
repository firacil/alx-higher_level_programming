#!/usr/bin/python3
"""
    script that list the first
    state objects from the database
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    """
        we are going to create engine
        and the have a new session to query
        on the database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).first()

    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        pass

    session.close()
