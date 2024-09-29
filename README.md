# Blogging API Project

This project is a **RESTful Blogging API** built with Django and Django REST Framework. The API allows users to create, read, update, and delete blog posts, manage categories, tags, comments, and likes, as well as user authentication and role-based access.

## Project Overview

The Blogging API is a backend application that provides endpoints for managing blog posts, user interactions, categories, tags, comments, and likes. Users can create an account, log in, and manage their own blog posts. Admins and editors have different roles with specific permissions for managing posts.

This API serves as the backend for a blogging platform, where developers can integrate frontend interfaces with the provided endpoints.

## Features

- User registration and authentication (JWT-based).
- CRUD operations for blog posts.
- Category and Tag management.
- Commenting and liking system for posts.
- Role-based access control (Admin, Editor, Reader).
- Search and filter functionality for posts.

## API Endpoints

### Posts
- `GET /api/posts/` - List all blog posts.
- `GET /api/posts/<id>/` - Retrieve a specific blog post by ID.
- `POST /api/posts/create/` - Create a new blog post (authenticated).
- `PUT /api/posts/update/<id>/` - Update an existing blog post (authenticated).
- `DELETE /api/posts/delete/<id>/` - Delete a blog post (authenticated).

### Categories
- `GET /api/categories/` - List all categories.
- `GET /api/categories/<id>/` - Retrieve a specific category by ID.

### Tags
- `GET /api/tags/` - List all tags.
- `GET /api/tags/<id>/` - Retrieve a specific tag by ID.

### Comments
- `POST /api/posts/<post_id>/comments/` - Add a comment to a post.
- `DELETE /api/posts/<post_id>/comments/<comment_id>/` - Delete a comment.

### Likes
- `POST /api/posts/<post_id>/like/` - Like a post.
- `DELETE /api/posts/<post_id>/like/` - Unlike a post.

### Users
- `POST /api/register/` - Register a new user.
- `POST /api/login/` - Obtain JWT tokens (login).



## Installation Prerequisites
- Python 3.8+
- Django 4.0+
- Django REST Framework
- MySQL or PostgreSQL (for production)

### Clone the Repository

```bash
git clone https://github.com/WuorBhang/blogging-api-project.git
cd blogging-api-project
