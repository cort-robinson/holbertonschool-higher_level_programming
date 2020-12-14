#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""
from sys import argv
from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    sesh = Session()

    for city in sesh.query(State.name, City.id, City.name).filter(
                           State.id == City.state_id).order_by(City.id):
        print("{}: ({}) {}".format(city[0], city[1], city[2]))

    sesh.close
