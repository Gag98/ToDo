"""Definition of the ToDo model and database table creation."""

from sqlalchemy import Column, String, Integer, Boolean
from todo.database.base import Base, engine


class ToDo(Base):
    """Class representing a ToDo item in the database.

    Attributes
    ----------
    id : int
        The primary key for the ToDo item.
    title : str
        The title or description of the ToDo item.
    is_complete : bool
        Indicates whether the ToDo item is completed. Default is False.
    """

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    is_complete = Column(Boolean, default=False)


# Create all tables in the database based on the defined models
Base.metadata.create_all(bind=engine)
