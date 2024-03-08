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

    print("\nplace_amenity table:")
    for row in place_amen:
        for obj in row:
            print(f"- {obj}")

    print("\nStates table:")
    for state in states:
        print(f"{state.name}", end="    ")

    print("\n\nCities table:")
    for city in cities:
        print(f"{city.name}", end="    ")

    print("\n\nPlaces table:")
    for place in places:
        print(f"{place.name}", end="    ")

    print("\n\nUsers table:")
    for user in users:
        print(f"{user.email}", end="    ")

    print()


if __name__ == "__main__":
    print_tables()
