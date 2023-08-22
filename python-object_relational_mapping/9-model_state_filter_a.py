#!/usr/bin/env python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def doit(username, password, database):
    # Create the engine
    x = f"""mysql+mysqldb://{username}:{password}@localhost:3306/{database}"""
    engine = create_engine(x, pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for State objects containing the letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    # Print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()


if __name__ == "__main__":
    # Get the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    doit(username, password, database)
