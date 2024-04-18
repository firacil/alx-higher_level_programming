#!/usr/bin/python3
"""
    script that prints all CIty objects
    from the database
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    """ impelemting here to make print all"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    stct = session.query(City, State).join(State)

    for city, state in stct.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
