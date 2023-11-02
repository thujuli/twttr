# TWTTR

![Application Architecture](docs/images/application-architecture.jpg?raw=true "Application Architecture")

#### Video Demo: [TWTTR]()

## Backgound

**TWTTR** is a simple _social media application_ project created using **Flask** and **Vue.js**. This application is designed to meet the needs of users who want to interact and share content in the form of text and images online. Some of the features include the ability for users to identify the most frequent posters and a unique characteristic where posts are only saved for 1 day, allowing new users a chance to top the leaderboard.

This project also serves as a learning tool, helping to enhance web development skills and adding significant value to a web developer's portfolio. Therefore, this application provides an excellent way to combine the power of web technology with my creativity in creating an engaging and beneficial social media platform."

## Requirements

**Docker**: You need Docker to manage and run containers containing the Flask and Vue.js applications, along with other required components for this project.

**Docker Compose**: Docker Compose allows you to define and run multiple containers simultaneously. This is essential for running a project that consists of multiple components, such as the backend and frontend.

**Internet Connection**: An internet connection is required to download the Docker images needed for this project, which are stored on Docker Hub. Additionally, an internet connection is required for the Minio service to upload image files.

## Dependencies and Packages

#### Backend (Flask)

- **Flask**: Python Framework for Website Development
- **Flask-Admin**: Flask Extensions for Managing Admin Panels
- **Flask-Cors**: Flask Extensions for Managing CORS
- **Flask-JWT-Extended**: Flask Extensions for Managing JWT Token
- **Flask-Login**: Flask Extensions for Managing Session
- **Flask-marshmallow**: Flask Extensions for Serialization/Deserialization
- **Flask-SQLAlchemy**: Flask Extension for SQL Database Communication using ORM
- **marshmallow-sqlalchemy**: Integrating SQLAlchemy with Marshmallow
- **pyscopg2**: Driver for Connecting to PostgreSQL with SQLAlchemy
- **celery**: Asynchronous Tasks and Task Scheduling
- **redis**: Interacting with a Redis Server
- **minio**: Minio SDK for Python Client
- **pytest**: Python Testing Framework
- **python-dotenv**: Read key-value pairs from .env
- **gunicorn**: WSGI HTTP Server for Python Application

#### Frontend (Vue.js)

- **vue**: Progressive JavaScript Framework for Frontend
- **vue-router**: Managing Routing for Vue
- **pinia**: State Management for Vue
- **axios**: Making HTTP Requests to the Server
- **headlessui/vue**: Unstyled Components
- **datatables.net-vue3**: DataTables for use as a component in Vue3
- **datatables.net-dt**: Styling Simply for DataTables
- **vue-sweetalert2**: Replacement JavaScript Popup
- **tailwindcss**: Utility-First CSS Framework

## Folder Structure in the Backend

```
.
├── app (Main Package of a Flask Project)
│   ├── __init__.py (Initialize Flask)
│   ├── admin (Admin Panel Configuration)
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── tweet.py
│   │   └── user.py
│   ├── api (Available Endpoints)
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── health.py
│   │   ├── leaderboard.py
│   │   ├── tweets.py
│   │   └── users.py
│   ├── core (Main Flask Configuration (Extensions and Settings))
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── extensions.py
│   │   └── security.py
│   ├── models (Representing Database Objects)
│   │   ├── __init__.py
│   │   ├── like.py
│   │   ├── token_blocklist.py
│   │   ├── tweet_count.py
│   │   ├── tweet.py
│   │   └── user.py
│   ├── schemas (Serializing Database Objects to JSON)
│   │   ├── __init__.py
│   │   ├── like.py
│   │   ├── tweet_count.py
│   │   ├── tweet.py
│   │   └── user.py
│   ├── services (Actions Related to Database Connectivity)
│   │   ├── __init__.py
│   │   ├── like.py
│   │   ├── token.py
│   │   ├── tweet_count.py
│   │   ├── tweet.py
│   │   └── user.py
│   ├── static (Static Assets)
│   │   └── assets
│   │       └── js
│   │           ├── login.js
│   │           └── register.js
│   ├── tasks (Executable Tasks)
│   │   ├── __init__.py
│   │   └── tweet.py
│   ├── templates (Frontend Using Jinja Templates)
│   │   ├── admin
│   │   │   └── index.html
│   │   └── auth
│   │       ├── login.html
│   │       └── register.html
│   ├── utils (Useful Utilities)
│   │   ├── __init__.py
│   │   ├── celery_app.py
│   │   ├── file.py
│   │   ├── login.py
│   │   ├── response.py
│   │   └── schedulers.py
│   ├── validators (User Input Validation)
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── tweet.py
│   │   └── user.py
│   └── views (Jinja Template Endpoints)
│       ├── __init__.py
│       └── routes.py
├── docker-compose-prod.yml (Docker Compose for Production)
├── docker-compose.yml (Docker Compose for Development)
├── Dockerfile (Dockerizing the Backend Service)
├── .env (Environment Variables)
├── .env.example (Example Environment Variables)
├── make_celery.py (Executor File for Running a Celery Instance)
├── manage.py (Executor File for Running a Flask Instance)
├── requirements.txt (List of Required Packages)
└── tests (Unit Testing for API Endpoints)
    ├── __init__.py
    ├── conftest.py
    ├── test_auth.py
    ├── test_health.py
    ├── test_tweets.py
    └── test_users.py
```

## Folder Structure in the Frontend

```
.
├── docker-compose-prod.yml (Docker Compose for Production)
├── docker-compose.yml (Docker Compose for Development)
├── Dockerfile (Dockerizing the Frontend Service)
├── .env (Environment Variables)
├── .env.example (Example Environment Variables)
├── index.html (Index HTML)
├── package.json (Information About This Project)
├── package-lock.json (Detail Information About This Project)
├── postcss.config.js (Configuration for PostCSS)
├── public (Public Directory)
│   └── favicon.ico
├── README.md (Simple Instructions to Run the Project)
├── src (Main Directory of a Vue Project)
│   ├── App.vue (Root App of Vue.js)
│   ├── assets (Static Assets)
│   │   ├── logo.svg
│   │   └── main.css
│   ├── components (UI Components)
│   │   ├── BtnLike.vue
│   │   ├── BtnPagination.vue
│   │   ├── Button.vue
│   │   ├── Card.vue
│   │   ├── Form.vue
│   │   ├── InputFile.vue
│   │   ├── Input.vue
│   │   ├── Modal.vue
│   │   ├── Navbar.vue
│   │   └── Textarea.vue
│   ├── composable (Reusable Functions)
│   │   ├── useAuth.js
│   │   └── useAxios.js
│   ├── main.js (Main Script)
│   ├── router (Manage Routes)
│   │   └── index.js
│   ├── service
│   │   └── axiosInstance.js
│   ├── stores (State Management)
│   │   └── authStore.js
│   └── views (View Components)
│       ├── Home.vue
│       ├── Leaderboard.vue
│       ├── Login.vue
│       └── Register.vue
├── tailwind.config.js (Configuration File for Tailwind CSS)
└── vite.config.js (Configuration File for Vite)
```

## Database Schema Design

![Database Schema](docs/images/database-schema.png?raw=true "Database Schema")

## Features

#### Admin Panel

![Admin Panel](docs/images/admin-panel.png?raw=true "Admin Panel")

#### Tweets Using Images or Text

![Create Tweet](docs/images/tweet.png?raw=true "Create Tweet")

#### Displaying Tweets with Pagination

![Home](docs/images/tweet.png?raw=true "Home")

#### Leaderboard of User Post Counts

![Leaderboard](docs/images/leaderboard.png?raw=true "Leaderboard")

#### Logout Notification

![Logout](docs/images/logout.png?raw=true "Logout")

#### Registration Page

![Registration](docs/images/registration.png?raw=true "Registration")

#### Login Page

![Login](docs/images/login.png?raw=true "Login")

## Deploy Project

#### Clone this Repository

```
# clone using ssh
git clone git@github.com:thujuli/twttr.git

# clone using https
git clone https://github.com/thujuli/twttr.git
```

#### Running the Backend Service

```
# change directory to backend
cd backend/

# execute docker-compose-prod.yml
docker compose -f docker-compose-prod up -d
```

#### Running the Frontend Service

```
# change directory to frontend
cd frontend/

# execute docker-compose-prod.yml
docker compose -f docker-compose-prod up -d
```
