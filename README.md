# Flix API

A REST API for managing a film catalogue: genres, actors, movies, and movie reviews. It is built with Django and Django REST Framework and uses JSON Web Tokens (JWTs) for authentication.

## Features

- CRUD endpoints for genres, actors, movies, and reviews
- Nested movie responses, including their genre, cast, and calculated average rating
- Catalogue statistics by genre and review rating
- JWT access, refresh, and verification endpoints
- Django model permissions for fine-grained access control
- Django admin interface

## Technology

- Python 3.13.5
- Django 6.1
- Django REST Framework 3.18
- Simple JWT
- SQLite (default development database)

## Getting started

### Prerequisites

- Python 3.13.5 (the version specified in `.python-version`)
- `pyenv` and `pyenv-virtualenv`, or another Python virtual environment manager

### Installation

Clone the repository and enter it:

```bash
git clone <repository-url>
cd flix-api
```

Activate the existing pyenv environment, if available:

```bash
pyenv activate flix-api
```

Alternatively, create a virtual environment and install the pinned dependencies:

```bash
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Apply database migrations and create an administrator account:

```bash
python manage.py migrate
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

The API is then available at `http://127.0.0.1:8000/api/v1/`, and the admin site at `http://127.0.0.1:8000/admin/`.

## Authentication and authorization

All catalogue endpoints require a valid JWT access token. Obtain one with a Django user’s credentials:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/authentication/token/ \
  -H 'Content-Type: application/json' \
  -d '{"username":"<username>","password":"<password>"}'
```

Use the returned access token on subsequent requests:

```http
Authorization: Bearer <access-token>
```

In addition to being authenticated, users need the Django permission that corresponds to the requested action: `view`, `add`, `change`, or `delete` for the relevant model. Superusers have all of these permissions. Assign permissions to other users through the admin site or Django groups.

Access tokens expire after one day; refresh tokens expire after seven days.

## API reference

All paths below are relative to `/api/v1/`.

| Resource | Endpoints | Notes |
| --- | --- | --- |
| Authentication | `POST authentication/token/` | Obtain an access/refresh token pair. |
|  | `POST authentication/token/refresh/` | Exchange a refresh token for a new access token. |
|  | `POST authentication/token/verify/` | Verify a token. |
| Genres | `GET`, `POST genres/` | List or create genres. |
|  | `GET`, `PUT`, `PATCH`, `DELETE genres/<id>/` | Retrieve, update, or delete a genre. |
| Actors | `GET`, `POST actors/` | List or create actors. |
|  | `GET`, `PUT`, `PATCH`, `DELETE actors/<id>/` | Retrieve, update, or delete an actor. |
| Movies | `GET`, `POST movies/` | List or create movies. GET returns nested genre/cast data and rating. |
|  | `GET`, `PUT`, `PATCH`, `DELETE movies/<id>/` | Retrieve, update, or delete a movie. |
|  | `GET movies/stats/` | Return catalogue and review statistics. |
| Reviews | `GET`, `POST reviews/` | List or create reviews. |
|  | `GET`, `PUT`, `PATCH`, `DELETE reviews/<id>/` | Retrieve, update, or delete a review. |

### Example requests

Create a genre:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/genres/ \
  -H 'Authorization: Bearer <access-token>' \
  -H 'Content-Type: application/json' \
  -d '{"name":"Science fiction"}'
```

Create an actor:

```json
{
  "name": "Sigourney Weaver",
  "birthday": "1949-10-08",
  "nationality": "USA"
}
```

Create a movie (`genre` and `actors` use database IDs):

```json
{
  "title": "Alien",
  "genre": 1,
  "release_date": "1979-05-25",
  "actors": [1],
  "resume": "The crew of a commercial space tug encounters a deadly extraterrestrial lifeform."
}
```

Create a review:

```json
{
  "movie": 1,
  "stars": 5,
  "comment": "A landmark science-fiction horror film."
}
```

`stars` must be an integer from 0 through 5. Actor nationality is currently limited to `USA` and `BRAZIL`.

## Development

Run the Django checks and test suite:

```bash
python manage.py check
python manage.py test
```

Create migrations after changing models, then apply them:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Production notes

The checked-in settings are development-oriented: debug mode is enabled, all hosts are allowed, and the Django secret key is present in source. Before deploying, load secrets and environment-specific settings from environment variables, set `DEBUG = False`, restrict `ALLOWED_HOSTS`, configure a production database and email backend, and serve static files through your deployment platform.

## License

This project is distributed under the [MIT License](LICENSE).
