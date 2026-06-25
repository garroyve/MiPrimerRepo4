import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")

def get_familia():
    rows = ["Amin", "Marce","Miranda"]
    return rows

@app.get("/superheroesDC")
def get_superheroesDC():
    rows = ["Superman","Batman","Flash","Linterna Verde","Mujer Maravilla","Aquaman","Shazam","Cyborg"]
    return rows

@app.get("/cursosPlatzi")
def get_cursos_platzi():
    rows = ["Python para principiantes","Desarrollo web con FastAPI","Machine Learning con Python"]
    return rows

