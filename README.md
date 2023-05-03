# FastAPI REST API with MongoDB

This is a sample project that demonstrates how to build a RESTful API with FastAPI and MongoDB.

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) - a modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- [MongoDB](https://www.mongodb.com/) - a document-oriented, NoSQL database used to store the data.
- [Pydantic](https://pydantic-docs.helpmanual.io/) - a data validation and settings management library that uses Python type annotations.
- [uvicorn](https://www.uvicorn.org/) - a lightning-fast ASGI server, built on top of [Starlette](https://www.starlette.io/).
- [Docker](https://www.docker.com/) - a containerization platform that makes it easy to package and deploy applications.
- [Docker Compose](https://docs.docker.com/compose/) - a tool for defining and running multi-container Docker applications.
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) - a fully-managed cloud database developed by the same people that build MongoDB.

## Getting Started

To get started with this project, follow these steps:

1.  Clone this repository to your local machine using `git clone https://github.com/JuanSebastianGB/fastapi-restapi-mongo.git`.
2.  Install the required dependencies by running `pip install -r requirements.txt`.
3.  Start the server by running `python main.py`.
4.  Go to `http://localhost:8000/docs` to view the API documentation and start testing the endpoints.

Another way

1.  Start the containers using Docker Compose

    Copy code

    `docker-compose up -d`

2.  The API should now be available at `http://localhost:8000`

## API Endpoints

Endpoint

Method

Description

`/users`

GET

Get all users

`/users/{id}`

GET

Get a user by ID

`/users`

POST

Create a new user

`/users/{id}`

PUT

Update a user by ID

`/users/{id}`

DELETE

Delete a user by ID

## Project Structure

The project is organized as follows:

markdownCopy code

- The `app` directory contains the main application code.
- The `database.py` file contains the database connection code.
- The `models.py` file contains the Pydantic models for the user data.
- The `routes` directory contains the FastAPI router for handling user-related API endpoints.
- The `services` directory contains the business logic for interacting with the database.
- The `main.py` file is the entry point for the application.
- The `requirements.txt` file lists the Python dependencies required by the project.

👍 If you find this project useful, give it a star!
