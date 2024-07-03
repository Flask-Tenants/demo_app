# Flask-Tenants Demo Application

This demo application demonstrates the implementation of Flask-Tenants for a multi-tenant blog platform. The application allows for the creation, retrieval, updating, and deletion of tenants and their respective blog posts. This README will guide you through the setup and usage of the application using Flask and Postman.

You may utilize a [Postman Collection](https://raw.githubusercontent.com/Flask-Tenants/demo_app/main/documentation/Flask-Tenants.postman_collection.json) designed for this demo application.

## Requirements

- alembic==1.13.2
- Flask==3.0.3
- SQLAlchemy==2.0.31
- Flask-SQLAlchemy==3.1.1
- flask-tenants==0.4.6
- psycopg2-binary==2.9.9
- python-dotenv==1.0.1

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Flask-Tenants/demo_app.git
    cd demo_app
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. Set environment variables for the application:

    ```sh
    export FLASK_APP=app.py
    export FLASK_ENV=development
    ```

2. Initialize the database:

    Create a `public` PostgreSQL schema and then run migrations

    ```sh
    flask db init
    flask db migrate
    flask db upgrade
    ```

3. Run the Flask application:

    ```sh
    flask run
    ```

## API Endpoints

### Public View

#### Create Tenant

- **Endpoint:** `POST /create_tenant`
- **Description:** Creates a new tenant.
- **Request Body:**

  ```json
  {
    "name": "tenant1",
    "domain_name": "tenant1.flasktenants.com",
    "phone_number": "123-456-7890",
    "address": "123 Example St"
  }
  ```

- **Response:**

  ```json
  {
    "message": "Tenant tenant1 created successfully",
    "tenant": {
      "address": "123 Example St",
      "domain_name": "tenant1.flasktenants.com",
      "id": 1,
      "name": "tenant1",
      "phone_number": "123-456-7890"
    }
  }
  ```

#### Read Tenant

- **Endpoint:** `GET /get_tenant/<tenant_name>`
- **Description:** Retrieves information about a specific tenant.
- **Response:**

  ```json
  {
    "address": "123 Example St",
    "id": 1,
    "name": "tenant1",
    "phone_number": "123-456-7890"
  }
  ```

#### Update Tenant

- **Endpoint:** `PUT /update_tenant/<tenant_name>`
- **Description:** Updates the information of a specific tenant.
- **Request Body:**

  ```json
  {
    "name": "tenant3",
    "domain_name": "tenant3.flasktenants.com",
    "phone_number": "123-456-7890",
    "address": "123 Example St"
  }
  ```

- **Response:**

  ```json
  {
    "message": "Tenant tenant3 updated successfully",
    "tenant": {
      "address": "123 Example St",
      "name": "tenant3",
      "phone_number": "123-456-7890"
    }
  }
  ```

#### Delete Tenant

- **Endpoint:** `DELETE /delete_tenant/<tenant_name>`
- **Description:** Deletes a specific tenant and its schema.
- **Response:**

  ```json
  {
    "message": "Tenant and its schema deleted successfully"
  }
  ```

### Tenant View

#### Create Post

- **Endpoint:** `POST /posts`
- **Description:** Creates a new post for a tenant.
- **Request Body:**

  ```json
  {
    "title": "The Great Commission",
    "body": "Go therefore and make disciples of all nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit, teaching them to observe all that I have commanded you. And behold, I am with you always, to the end of the age.",
    "author": "Jesus"
  }
  ```

- **Response:**

  ```json
  {
    "message": "Post created successfully"
  }
  ```

#### Read Posts

- **Endpoint:** `GET /posts`
- **Description:** Retrieves all posts for a tenant.
- **Response:**

  ```json
  [
    {
      "author": "Jesus",
      "body": "Go therefore and make disciples of all nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit, teaching them to observe all that I have commanded you. And behold, I am with you always, to the end of the age.",
      "id": 1,
      "title": "The Great Commission"
    }
  ]
  ```

#### Update Post

- **Endpoint:** `PUT /posts/<post_id>`
- **Description:** Updates a specific post for a tenant.
- **Request Body:**

  ```json
  {
    "title": "Salvation",
    "body": "If you confess with your mouth that Jesus is Lord and believe in your heart that God raised him from the dead, you will be saved.",
    "author": "Paul"
  }
  ```

- **Response:**

  ```json
  {
    "message": "Post updated successfully"
  }
  ```

#### Delete Post

- **Endpoint:** `DELETE /posts/<post_id>`
- **Description:** Deletes a specific post for a tenant.
- **Response:**

  ```json
  {
    "message": "Post deleted successfully"
  }
  ```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
