# tpctest

A lightweight Python test suite and connection harness for the Trino DB-API driver (`trino-python-client`), built with `pytest`, `ruff`, and `pre-commit`.

---

## Architecture & Project Layout

This project uses a standard `src`-layout to separate package implementation from test execution:

```text
tpctest/
├── .github/
│   └── workflows/
│       └── ci.yml               # GitHub Actions CI matrix
├── src/
│   ├── __init__.py
│   └── connection.py            # Trino DB-API wrappers & query helpers
├── tests/
│   └── test_tpcconnection.py    # Unit tests with mocks
├── .gitattributes
├── .gitignore
├── .pre-commit-config.yaml      # Git pre-commit configuration
├── pyproject.toml               # Build system, dependencies & tooling config
└── README.md
```
Prerequisites
Python: 3.10, 3.11, or 3.12+

OS: Linux / WSL2 (Ubuntu recommended)

Build System: setuptools with pyproject.toml support

## Getting Started
### 1. Clone & Set Up Environment
```Bash
# Clone the repository
git clone [https://github.com/xsgao-github/tpctest.git](https://github.com/xsgao-github/tpctest.git)
cd tpctest

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Upgrade base tooling
pip install --upgrade pip setuptools
```

### 2. Install Dependencies
Install development dependencies and register the local package in editable mode:

```Bash
pip install pytest pytest-cov ruff pre-commit trino
pip install -e .
```

### 3. Running Tests
Execute the test suite using pytest through your environment's Python runner:

```Bash
# Run tests
python -m pytest

# Run tests with verbose output and coverage
python -m pytest -v --cov=src
```

### 4. Code Quality & Pre-commit Hooks

This project enforces code formatting, linting, and automated testing via Ruff and pre-commit.

Install Pre-commit Hooks
To automatically lint and test code prior to every commit, install the hooks locally:

```Bash
pip install pre-commit
pre-commit install

# Run all pre-commit hooks
pre-commit run --all-files

# Run Ruff linter and formatter individually
ruff check . --fix
ruff format --check .
```

### 5. Continuous Integration
GitHub Actions automatically runs on pushes and pull requests to main across Python versions 3.10, 3.11, and 3.12. The pipeline verifies:

Code syntax and linting via Ruff

Code formatting adherence

Full test execution via pytest

XML coverage generation for reporting
