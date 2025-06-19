from sqlmodel import select, Session
from models import Movie
from typing import List
from fastapi import HTTPException


def get_movies(session: Session) -> List[Movie]:
    statement = select(Movie)
    results = session.exec(statement)
    return results.all()

def get_movies_by_title(session: Session, title: str) -> List[Movie]:
    statement = select(Movie).where(Movie.title.ilike(f"{title}%"))
    results = session.exec(statement)
    return results.all()

def get_movie_by_id(session: Session, movie_id: int) -> Movie:
    statement = select(Movie).where(Movie.id == movie_id)
    results = session.exec(statement)
    movie = results.first()
    if not movie:
        raise HTTPException(status_code=404, detail=f"Movie with id {movie_id} not found")
    return movie

def create_movie(session: Session, movie: Movie) -> Movie:
    session.add(movie)
    session.commit()
    session.refresh(movie)
    return movie

def update_movie(session: Session, movie_id: int, movie_data: Movie) -> Movie:
    movie = get_movie_by_id(session, movie_id)
    for key, value in movie_data.dict(exclude_unset=True).items():
        setattr(movie, key, value)
    session.commit()
    session.refresh(movie)
    return movie

def delete_movie(session: Session, movie_id: int) -> None:
    movie = get_movie_by_id(session, movie_id)
    session.delete(movie)
    session.commit()
    return None
