# Hello World Flask App

A simple Flask application that displays "Hello, World!" and personalized greetings. The project includes unit tests (pytest), BDD tests (Behave), and a CI/CD pipeline using GitHub Actions.

## Features

* Displays "Hello, World!" at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
* Displays personalized greetings at `/greet/<name>` (e.g., "Hello, Alice!" for `/greet/Alice`)
* Displays the current date at `/date` (e.g., "Current date: 2025-04-25")
* Displays submit form at `/submit`
* Handles invalid routes with a 404 error
* Unit tests verify main page, greetings, date, and error handling
* BDD tests ensure user requirements are met
* Automated CI/CD pipeline runs tests on every push

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/username/hello-world-flask.git
cd hello-world-flask
```

### 2. Create and activate a virtual environment

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
python app/main.py
```

Access the app at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Running Tests

### Unit tests

```bash
python -m pytest tests/
```

### BDD tests

```bash
behave features/
```

## CI/CD Pipeline

* GitHub Actions workflow: `.github/workflows/ci.yml`
* Triggers: `push` and `pull_request` events on `main`
* Steps:

  1. Set up Python environment on Ubuntu
  2. Install dependencies from `requirements.txt`
  3. Run unit tests with pytest
  4. Run BDD tests with behave
* View workflow logs in GitHub Actions tab

## Development Notes

* Flask app main file: `app/main.py` (add routes/features as needed)
* Unit tests: `tests/` folder
* BDD tests: `features/` folder
* Optional: Add `static/favicon.ico` to avoid 404

## Troubleshooting

* File not found: ensure `app/main.py` exists
* Dependency issues: verify packages in `requirements.txt`
* Pipeline failures: check GitHub Actions logs

## Future Improvements

* Add deployment steps (Heroku, Vercel)
* Include code linting (flake8)
* Expand unit and BDD tests
