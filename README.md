#📚 Library Project API 📚
Welcome to the Library Project API, developed using Django Rest Framework (DRF). This API allows you to manage a library system with various features and endpoints. Let's dive into the cool features of this project! 🎉

##Features
###🔒 User Authentication: Secure your API with TokenAuthentication to handle user login, logout, registration, password reset, and password change functionalities. Keep your users' data safe and their access controlled.

✏️ CRUD Operations: Perform Create, Read, Update, and Delete operations on various resources of the library. Manage books, authors, borrowers, and more with ease.

📖 Documentation with Swagger and Redoc: We believe in making API documentation as cool as the project itself! Swagger and Redoc have been integrated to provide interactive and user-friendly API documentation. You can easily explore and test the API endpoints through these awesome tools.

API Endpoints
Here's an overview of the available API endpoints:

Authentication

POST /api/token/: Get an access token by providing valid credentials.
POST /api/token/refresh/: Refresh an expired access token.
POST /api/token/verify/: Verify the validity of an access token.
Users

POST /api/register/: Register a new user.
POST /api/login/: Log in an existing user.
POST /api/logout/: Log out the currently authenticated user.
POST /api/password/reset/: Reset the user's password.
POST /api/password/change/: Change the user's password.
Books

GET /api/books/: Get a list of all books.
POST /api/books/: Create a new book.
GET /api/books/{id}/: Get details of a specific book.
PUT /api/books/{id}/: Update details of a specific book.
DELETE /api/books/{id}/: Delete a specific book.
Authors

GET /api/authors/: Get a list of all authors.
POST /api/authors/: Create a new author.
GET /api/authors/{id}/: Get details of a specific author.
PUT /api/authors/{id}/: Update details of a specific author.
DELETE /api/authors/{id}/: Delete a specific author.
Borrowers

GET /api/borrowers/: Get a list of all borrowers.
POST /api/borrowers/: Create a new borrower.
GET /api/borrowers/{id}/: Get details of a specific borrower.
PUT /api/borrowers/{id}/: Update details of a specific borrower.
DELETE /api/borrowers/{id}/: Delete a specific borrower.
Getting Started
To get started with the Library Project API, follow these steps:

Clone the repository: git clone https://github.com/your-username/library-api.git
Install the required dependencies: pip install -r requirements.txt
Apply the database migrations: python manage.py migrate
Create a superuser to access the admin interface: python manage.py createsuperuser
Run the development server: python manage.py runserver
Now you can access the API at http://localhost:8000/api/ and the admin interface at http://localhost:8000/admin/.

API Documentation
Don't forget to check out our cool API documentation using Swagger and Redoc! You can access it at http://localhost:8000/swagger/ and http://localhost:8000/redoc/.

Let's Get Started! 🚀
The Library Project API is all set and ready to help you manage your library efficiently. Feel free to explore the API endpoints and use them in your projects. If you have any questions or need assistance, don't hesitate to reach out to our friendly team.

Happy coding! 😎📚
