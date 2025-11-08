#!/usr/bin/env python3

from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():
    fake = Faker()

    # Clear existing records
    Pet.query.delete()

    species_list = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']
    pets = []

    # Create 10 random pets
    for n in range(10):
        pet = Pet(
            name=fake.first_name(),
            species=rc(species_list)
        )
        pets.append(pet)

    # Add to database
    db.session.add_all(pets)
    db.session.commit()

    print("✅ Database seeded with 10 random pets!")
