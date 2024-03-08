#!/usr/bin/python3
from models import DBStorage
from models.place import place_amenity
from sqlalchemy import select
from models.state import State
from models.city import City
from models.place import Place
from models.user import User

def print_tables():
    session = DBStorage()
    session.reload()
    engine = session.get_engine()

    with engine.connect() as connection:
        place_amen = connection.execute(select(place_amenity)).fetchall()
        states = connection.execute(select(State)).fetchall()
        cities = connection.execute(select(City)).fetchall()
        places = connection.execute(select(Place)).fetchall()
        users = connection.execute(select(User)).fetchall()

    print("\nStates table:")
    for state in states:
        print(f"{state.name}", end="  | ")

    print("\n\nCities table:")
    for city in cities:
        print(f"{city.name}", end="  | ")

    print("\n\nPlaces table:")
    for place in places:
        print(f"{place.name}", end="  | ")

    print("\n\nUsers table:")
    for user in users:
        print(f"{user.email}", end="  | ")

    i = -1
    print("\n\nplace_amenity table:")
    print("| ", end="")
    for row in place_amen:
        for obj in row:
            if i < 2:
                print(f"{obj}", end=" | ")
                i += 1
            else:
                print(f"\n| {obj}", end=" | ")
                i = 0

    print()


if __name__ == "__main__":
    print_tables()
