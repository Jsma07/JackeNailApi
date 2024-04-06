# from fastapi import FastAPI, Path,Query
# from pydantic import BaseModel, Field
# from typing import Optional, List
# import datetime 


# app = FastAPI()
# app.title = "Mi primera api"
# app.version= "2.2.2"

# class Movie(BaseModel):
#      id: int
#      name: str 
#      description: str
#      category: str
#      studio: str  
#      year: int
# class MovieCrear(BaseModel):
#      id: int
#      name: str = Field(min_length=5, max_length=15, default="pelicula")
#      description: str = Field(min_length=15, max_length= 100)
#      category: str = Field(min_length=5, max_length= 100)
#      studio: str  
#      year: int =  Field(le= datetime.date.today().year, ge=1900)
    
#      model_config= {'json_schema_extra': {'example':{
#          'id': 1,
#          'name': "mi pelicula",
#          'description': 'Description...',
#          'category': 'Accion',
#          'studio': 'Marvel',
#          'year': 2024
#      }}}
# class MovieActualizar(BaseModel):
#      name: str 
#      description: str
#      category: str
#      studio: str  
#      year: int

# movies: List[MovieCrear] = []


# @app.get("/movies/{id}", tags=['Movies'])
# def get_movie(id: int= Path(gt=0))-> Movie | dict:
#     for movie in movies:
#         if movie.id == id:
#             return movie.model_dump()
#     return {"message": "Película no encontrada"}

# @app.get("/", tags=['Home'])
# async def root():
#     return  "hola mundo"

# @app.get("/movies", tags=['Movies'])
# async def get_movies() -> List[Movie]: 
#     return [movie.model_dump() for movie in movies]

# @app.get("/moviesCategory", tags=['Movies'])
# def get_movie_by_category(category: str = Query(min_length=5, max_length=20)) -> Movie | dict:
#    for movie in movies:
#        if movie.category == category:
#            return movie.model_dump()
#    return {}
       
# @app.post("/movieCrear", tags=['Movies'])
# def crear_movie(movie: MovieCrear)-> List[Movie]:

#     movies.append(movie)

    
#     return [movie.model_dump() for movie in movies]

# @app.put("/movies/{id}", tags=['Movies'])
# def actualizarMovie(id: int, movie: MovieActualizar)-> List[Movie]:
#     for item in movies:
#         if item['id'] == id:
#             item['name'] = movie.name,
#             item['description'] = movie.description,
#             item['category'] = movie.category,
#         item['studio'] = movie.studio
#     return [movie.model_dump() for movie in movies]

# @app.delete('/movies/{id}', tags=['Movies'])
# def eliminarMovie(id: int)-> List[Movie]:
#     for movie in movies:
#         if movie['id'] == id:
#             movies.remove(movie)
#     return [movie.model_dump() for movie in movies]

        
