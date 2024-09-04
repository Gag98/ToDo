"""Entry point for running the ToDo application using Uvicorn."""

import os
import uvicorn
from todo.app import app

if __name__ == '__main__':
    """Start the Uvicorn server to run the FastAPI application.

    The server is configured to run the application on the specified host and port.
    The port is retrieved from the environment variable PORT, with a default of 5000 if not set.

    Parameters
    ----------
    host : str
        The IP address on which the server will run. Default is "0.0.0.0".
    port : int
        The port on which the server will run. Default is 5000.
    log_level : str
        The log level for Uvicorn. Default is "info".
    """
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")

