from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models
from pydantic import BaseModel
from .database import SessionLocal, engine


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


class ArtistBase(BaseModel):
    artistId: int
    name: str


class AlbumBase(BaseModel):
    albumId: int
    title: str
    artistId: int


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/artists/{name}", status_code=status.HTTP_200_OK)
async def read_artists(name: str, db: Session = Depends(get_db)):
    query = f"%{name}%"
    artist = db.query(models.Artist).where(models.Artist.name.like(query)).first()
    if artist is None:
        raise HTTPException(status_code=404, detail="Artist Name not in Database")
    return artist


@app.get("/albums/{artistId}", status_code=status.HTTP_200_OK)
async def read_albums(artistId: int, db: Session = Depends(get_db)):
    albums = db.query(models.Album).where(models.Album.artistId == artistId).all()
    if albums is None:
        raise HTTPException(
            status_code=404,
            detail="This artist id does not exist or have no albums in database",
        )
    return albums
