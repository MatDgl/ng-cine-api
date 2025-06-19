from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from crud.movie import get_movies, get_movie_by_id, get_movies_by_title, create_movie, update_movie, delete_movie
from models import Movie
from database import get_session

movie_router = APIRouter()

@movie_router.get("/movie")
def read_movies(session: Session = Depends(get_session)):
    """
    Retrieve a list of movies from the database.
    """
    movies = get_movies(session)
    return movies

@movie_router.get("/movie/search")
def search_movies(title: str, session: Session = Depends(get_session)):
    """
    Search for movies by title.
    """
    movies = get_movies_by_title(session, title)
    return movies

@movie_router.get("/movie/{movie_id}", response_model=Movie)
def read_movie(movie_id: int, session: Session = Depends(get_session)):
    """
    Retrieve a movie by its ID.
    """
    return get_movie_by_id(session, movie_id)

@movie_router.post("/movie", response_model=Movie)
def create_new_movie(movie: Movie, session: Session = Depends(get_session)):
    """
    Create a new movie in the database.
    """
    created_movie = create_movie(session, movie)
    return created_movie

@movie_router.put("/movie/{movie_id}", response_model=Movie)
def update_existing_movie(movie_id: int, movie_data: Movie, session: Session = Depends(get_session)):
    """
    Update an existing movie by its ID.
    """
    try:
        updated_movie = update_movie(session, movie_id, movie_data)
        return updated_movie
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@movie_router.delete("/movie/{movie_id}")
def delete_existing_movie(movie_id: int, session: Session = Depends(get_session)):
    """
    Delete a movie by its ID.
    """
    try:
        delete_movie(session, movie_id)
        return {"detail": "Movie deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    