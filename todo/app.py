"""Initialization of the FastAPI application and template engine."""

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

# Initializing the FastAPI application
app = FastAPI()

# Connecting a static file directory
app.mount("/static", StaticFiles(directory="todo/static"), name="static")

# Setting up Jinja2 templates to render HTML
templates = Jinja2Templates(directory="todo/templates")

# Import application routes
from todo.routes import home