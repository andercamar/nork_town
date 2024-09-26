## Description
To-Do List App
Description
Nork-Town is a weird place. Crows cawk the misty morning while old men squint. It’s a small
town, so the mayor had a bright idea to limit the number of cars a person may possess. One
person may have up to 3 vehicles. The vehicle, registered to a person, may have one color,
‘yellow’, ‘blue’ or ‘gray’. And one of three models, ‘hatch’, ‘sedan’ or ‘convertible’.
Carford car shop want a system where they can add car owners and cars. Car owners may
not have cars yet, they need to be marked as a sale opportunity. Cars cannot exist in the
system without owners.

## Requirements

- Setup the dev environment with docker
- Using docker compose with as many volumes as it takes
- Use Python’s Flask framework and any other library
- Use any SQL database
- Secure routes
- Write tests

## Technologies Used

- Backend: Python with Flask
- Database: PostgreSQL
- Authentication: Flask-JWT-Extended
- Automated Testing: Pytest
- Development Environment: Docker and Docker Compose

## Prerequisites
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Setting Up the Environment

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/nork-town.git
   cd nork-town

2. **Start Containers with Docker Compose
   ```bash
   docker compose up --build

3. ** Initialize the database
   ```bash
   docker compose exec api python manage.py init-db

## Usage
- **Access the application at:** `http://localhost:5000`
- **Use a client like [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/) to test the routes.**

### Routes
- **Authentication**
- `POST /login`: Login and obtain JWT token.

- **Persons**
- `POST /person`: Create a new person.
- `GET /person`: List all persons.
- `GET /person/<id>`: Get a person.
- `PUT /person/<id>`: Update person.
- `DELETE /person/<id>`: Delete a person.

- **Vehicles**
- `POST /cars`: Add a new car.
- `GET /cars`: List all cars.
- `GET /cars/<id>`: Get a car.
- `PUT /cars/<id>`: Update car.
- `DELETE /cars/<id>`: Delete a car.

## Tests

1. **Start the application container
   ```bash
   docker compose up -d

2. **Execute the tests with the command
   ```bash
   docker compose exec api pytest

