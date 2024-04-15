import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    last_name =  Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_name=  Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    character_name=  Column(String(250), nullable=False)

class FavoritesPlanets(Base):
    __tablename__ = 'FavoritePlanets'
    id = Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)

class FavoritesCharacters(Base):
    __tablename__ = 'FavoriteCharacters'
    id = Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    character_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters)
      


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')




