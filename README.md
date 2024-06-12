# FastAPI Post Management API

This repository contains code for a FastAPI-based API that allows users to manage posts. The API supports authentication using JWT tokens and implements caching for improved performance.

## Features

- User authentication using JWT tokens
- Endpoints for creating, reading, updating, and deleting posts
- Response caching for improved performance

## Setup

1. Clone the repository:
2. Install dependencies:
3. Run the FastAPI server:
The API will be available at http://localhost:8000.

## API Endpoints

- **POST /signup**: Sign up a new user.
- **POST /login**: Log in a user and get an authentication token.
- **POST /add_post**: Add a new post.
- **DELETE /delete_post/{post_id}**: Delete a post by ID.
- **GET /get_posts**: Get all user's posts.

For detailed documentation on each endpoint, refer to the API documentation or the codebase.

## Technologies Used

- FastAPI: Web framework for building APIs with Python.
- SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library.
- JWT (JSON Web Tokens): Standard for securely transmitting information between parties.
- cachetools: Library for caching in Python.

