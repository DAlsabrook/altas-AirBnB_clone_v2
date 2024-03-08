#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.engine.db_storage import DBStorage
from sqlalchemy import select, Table
from models.base_model import Base
from models.place import place_amenity
# creation of a State
state = State(name="California")
state.save()
# creation of a City
city = City(state_id=state.id, name="San Francisco")
city.save()
# creation of a User
user = User(email="john@snow.com", password="johnpwd")
user.save()
# creation of 2 Places
place_0 = Place(user_id=user.id, city_id=city.id, name="House 0")
place_0.save()
place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()
place_2 = Place(user_id=user.id, city_id=city.id, name="House Bla")
place_2.save()
place_3 = Place(user_id=user.id, city_id=city.id, name="House 2")
place_3.save()
# creation of 3 various Amenity
amenity_0 = Amenity(name="my_name_0")
amenity_0.save()
amenity_1 = Amenity(name="my_name_1")
amenity_1.save()
amenity_2 = Amenity(name="my_name_2")
amenity_2.save()
amenity_3 = Amenity(name="my_name_3")
amenity_3.save()
# link place_1 with 2 amenities
place_0.amenities.append(amenity_0)
place_0.amenities.append(amenity_1)
place_0.amenities.append(amenity_2)
# link place_2 with 3 amenities
place_1.amenities.append(amenity_1)

place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)
place_2.save()
storage.save()

places = [place_0, place_1, place_2, place_3]
for place in places:
    if place is not None:
        print(f"place: {place.name}")
        for amenity in place.amenities:
            if place.amenities is None:
                continue
            print(f"\tplace.amenities: {amenity.name}")


session = DBStorage()
session.reload()
engine = session.get_engine()
with engine.connect() as connection:
    result = connection.execute(select(place_amenity)).fetchall()
print("\nplace_amenity table :")
for row in result:
    for obj in row:
        print(obj)


# print(amenity_0.place[0].id)
# print(place_0.id)
# print(storage.all(Place))
