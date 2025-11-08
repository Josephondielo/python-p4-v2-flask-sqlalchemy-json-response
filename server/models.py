from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Use naming conventions for migrations
metadata = MetaData()

# Create SQLAlchemy database instance
db = SQLAlchemy(metadata=metadata)

# Define Pet model
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    def __repr__(self):
        return f'<Pet {self.id}, {self.name}, {self.species}>'
