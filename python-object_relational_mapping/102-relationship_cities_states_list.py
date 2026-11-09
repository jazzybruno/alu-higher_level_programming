#!/usr/bin/python3
"""Lists every City with its State name using one query."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import joinedload, sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    query = session.query(City).options(joinedload(City.state))
    for city in query.order_by(City.id).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
