# Hello World Flask App

A simple Flask application that displays "Hello, World!" at the root URL (`/`). The project includes unit tests (pytest), behavior-driven development (BDD) tests (Behave), and a CI/CD pipeline using GitHub Actions.

## Features
- Displays "Hello, World!" at `http://127.0.0.1:5000/`.
- Displays personalized greetings at `http://127.0.0.1:5000/greet/<name>` (e.g., "Hello, Alice!" for `/greet/Alice`).
- Displays the current date at `http://127.0.0.1:5000/date` (e.g., "Current date: 2025-04-25").
- Displays submit form at `http://127.0.0.1:5000/submit`
- Handles invalid routes with a 404 error.
- Unit tests verify the main page, greetings, date, and error handling
- BDD tests ensure user requirements are met.
- Automated CI/CD pipeline runs tests on every push.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/username/hello-world-flask.git