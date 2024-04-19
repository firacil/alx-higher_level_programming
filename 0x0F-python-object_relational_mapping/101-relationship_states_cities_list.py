#!/usr/bin/python3
"""
    script that lists all state objects, and corresponding
    city objects, contained in the database
"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from sys import argv


if __name__ == "__main__":
    """
        implementing the script above
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).outerjoin(City) \
                    .order_by(State.id, City.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
