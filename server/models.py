from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Numeric
from sqlalchemy.orm import relationship


class Artist(Base):
    __tablename__ = "artists"

    artistId = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class Album(Base):
    __tablename__ = "albums"

    albumId = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    artistId = Column(Integer)


class Track(Base):
    __tablename__ = "tracks"

    trackId = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    albumId = Column(Integer)
    mediaTypeId = Column(Integer)
    genreId = Column(Integer)
    composer = Column(String)
    milliseconds = Column(Integer)
    bytes = Column(Integer)
    unitPrice = Column(Numeric)
