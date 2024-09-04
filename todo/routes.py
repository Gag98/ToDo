"""Route handlers for the ToDo application using FastAPI."""

from fastapi import Request, Depends, Form
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER, HTTP_302_FOUND

from todo.config import settings
from todo.database.base import get_db
from todo.app import app, templates
from todo.models import ToDo


@app.get("/")
def home(request: Request, db_session: Session = Depends(get_db)):
    """Handles the GET request for the home page.

    Fetches all ToDo items from the database and renders the home page template.

    Parameters
    ----------
    request : Request
        The request object.
    db_session : Session, optional
        The database session used to query ToDo items. Automatically provided by FastAPI dependency injection.

    Returns
    -------
    TemplateResponse
        The rendered home page with a list of ToDo items.
    """
    todos = db_session.query(ToDo).all()
    return templates.TemplateResponse(
        "todo/index.html",
        {
            "request": request,
            "app_name": settings.app_name,
            "todo_list": todos,
        },
    )


@app.post("/add")
def add(title: str = Form(...), db_session: Session = Depends(get_db)):
    """Handles the POST request to add a new ToDo item.

    Creates a new ToDo item and saves it to the database.

    Parameters
    ----------
    title : str
        The title of the new ToDo item. Provided via form data.
    db_session : Session, optional
        The database session used to add the new ToDo item. Automatically provided by FastAPI dependency injection.

    Returns
    -------
    RedirectResponse
        A redirect to the home page.
    """
    new_todo = ToDo(title=title)
    db_session.add(new_todo)
    db_session.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=HTTP_303_SEE_OTHER)


@app.get("/update/{todo_id}")
def update(todo_id: int, db_session: Session = Depends(get_db)):
    """Handles the GET request to update a ToDo item.

    Toggles the completion status of the specified ToDo item.

    Parameters
    ----------
    todo_id : int
        The ID of the ToDo item to update.
    db_session : Session, optional
        The database session used to update the ToDo item. Automatically provided by FastAPI dependency injection.

    Returns
    -------
    RedirectResponse
        A redirect to the home page.
    """
    todo = db_session.query(ToDo).filter(ToDo.id == todo_id).first()
    todo.is_complete = not todo.is_complete
    db_session.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=HTTP_302_FOUND)


@app.get("/delete/{todo_id}")
def delete(todo_id: int, db_session: Session = Depends(get_db)):
    """Handles the GET request to delete a ToDo item.

    Removes the specified ToDo item from the database.

    Parameters
    ----------
    todo_id : int
        The ID of the ToDo item to delete.
    db_session : Session, optional
        The database session used to delete the ToDo item. Automatically provided by FastAPI dependency injection.

    Returns
    -------
    RedirectResponse
        A redirect to the home page.
    """
    todo = db_session.query(ToDo).filter_by(id=todo_id).first()
    db_session.delete(todo)
    db_session.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=HTTP_302_FOUND)