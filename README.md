```markdown
# CryptoStream: Modular ETL Pipeline for Bitcoin Price Data

## Overview

CryptoStream is an end-to-end data engineering project that fetches real-time Bitcoin pricing data using the CoinGecko API, processes it through a modular ETL pipeline, and stores it in a PostgreSQL database. This project demonstrates best practices in data engineering, including modular Python code, containerization with Docker, orchestration using Docker Compose, and automation through a Makefile.

## Project Structure

```
crypto_stream/
├── .env                # Environment configuration file
├── .gitignore          # Ignore virtual environments, __pycache__, etc.
├── Dockerfile          # Container build instructions for the ETL app
├── docker-compose.yml  # Defines services (db and etl) for Docker Compose
├── Makefile            # Run common commands (build, up, run, etc.)
├── README.md           # This documentation file
└── src/                # Source code for the ETL pipeline
    ├── __init__.py
    ├── extractor.py    # Module to fetch data from CoinGecko API
    ├── transformer.py  # Module to transform raw API data into structured format
    ├── loader.py       # Module to load data into PostgreSQL
    ├── db_setup.py     # Module to set up the database and create necessary tables
    └── main.py         # Main orchestrator of the ETL process
```

## Setup Instructions

### 1. Environment Setup (Local)

- **Python & Virtual Environment:**
  1. Ensure you have Python 3.9+ installed.
  2. Create and activate a virtual environment:
     ```bash
     python -m venv env
     source env/bin/activate      # On Windows: env\Scripts\activate
     ```
  3. Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

- **Environment Variables:**
  Create a file named `.env` in the project root with the following content:
  ```
  # Database settings (Local Mode)
  DB_HOST=localhost
  DB_PORT=5432
  DB_NAME=crypto_db
  DB_USER=postgres
  DB_PASSWORD=password
  ```

- **Git Configuration:**
  Ensure your `.gitignore` file includes:
  ```
  # Ignore virtual environment directories
  env/
  venv/

  # Ignore Python cache directories and compiled files
  __pycache__/
  *.py[cod]
  *.pyo
  ```

### 2. Running Locally

- **Run the ETL Pipeline:**
  With the virtual environment activated, execute:
  ```bash
  python src/main.py
  ```
  This command will:
  - Create the PostgreSQL database and table (if not already present).
  - Extract data from the CoinGecko API.
  - Transform the data.
  - Load the data into your local PostgreSQL instance.

### 3. Running with Docker Compose

- **Important Note on Environment Variables:**
  When running via Docker Compose, update your `.env` file to set:
  ```
  DB_HOST=db
  ```
  This tells your ETL container to connect to the PostgreSQL container (named **db** in docker-compose.yml). When running locally with main.py, use `localhost`.

- **Using Docker Compose:**
  1. Build and start the services:
     ```bash
     docker-compose up --build
     ```
  2. The PostgreSQL container (service: `db`) will run on its internal port 5432, while host port mapping (if set) is used only for external connections.
  3. Your ETL container will automatically execute the ETL process, including database setup, extraction, transformation, and loading.

### 4. Using the Makefile

You can execute common commands via the provided Makefile:

- **Build the Docker Images:**
  ```bash
  make build
  ```
- **Start All Services:**
  ```bash
  make up
  ```
- **Run the ETL Job Once:**
  ```bash
  make run
  ```
- **View Logs:**
  ```bash
  make logs
  ```
- **Open a PostgreSQL Shell:**
  ```bash
  make db_shell
  ```
- **Stop and Remove Containers and Volumes:**
  ```bash
  make clean
  ```

## Summary

CryptoStream is a comprehensive project designed to showcase my data engineering skills. It features:

- A modular Python ETL pipeline.
- Integration with a real-time API (CoinGecko) for Bitcoin pricing data.
- Automated database setup and data ingestion.
- Containerization and orchestration with Docker and Docker Compose.
- Simplified command execution via a Makefile.

**Important Configuration Notes:**

- **Docker Mode:**  
  Set `DB_HOST=db` in your `.env` file to allow inter-container communication.
  
- **Local Mode:**  
  Set `DB_HOST=localhost` when running directly with `python src/main.py`.

This project is ready for deployment and serves as an excellent demonstration piece for technical interviews.
```