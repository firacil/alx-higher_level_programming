#!/usr/bin/python3
"""
    script that list all state
    which contain letter 'a'
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

    states = session.query(State).filter(State.name.like('%a%')) \
                    .order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
