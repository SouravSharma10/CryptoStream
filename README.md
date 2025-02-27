CryptoStream: Modular ETL Pipeline for Bitcoin Price Data
===========================================================

Overview
--------
CryptoStream is an end-to-end data engineering project that fetches real-time Bitcoin pricing data using the CoinGecko API, processes it through a modular ETL pipeline, and stores it in a PostgreSQL database. This project demonstrates best practices in data engineering, including modular Python code, containerization with Docker, orchestration using Docker Compose, and automation via a Makefile.

Setup Instructions
------------------

1. Environment Setup (Local)
   ----------------------------
   Python & Virtual Environment:
   1. Ensure you have Python 3.9+ installed.
   2. Create and activate a virtual environment:
      
         python -m venv env
         source env/bin/activate      # On Windows: env\Scripts\activate

   3. Install dependencies:
      
         pip install -r requirements.txt

   Environment Variables:
   Create a file named ".env" in the project root with the following content:

         # Database settings (Local Mode)
         DB_HOST=localhost
         DB_PORT=5432
         DB_NAME=crypto_db
         DB_USER=postgres
         DB_PASSWORD=password

   Git Configuration:
   Ensure your ".gitignore" file includes entries to ignore virtual environment directories and Python cache files:

         # Ignore virtual environment directories
         env/
         venv/

         # Ignore Python cache directories and compiled files
         __pycache__/
         *.py[cod]
         *.pyo

2. Running Locally
   ----------------
   With your virtual environment activated, run the ETL pipeline by executing:

         python src/main.py

   This command will:
   - Create the PostgreSQL database and table (if not already present).
   - Extract data from the CoinGecko API.
   - Transform the data.
   - Load the data into your local PostgreSQL instance.

3. Running with Docker Compose
   -----------------------------
   Important Note on Environment Variables:
   When running via Docker Compose, update your ".env" file to set:

         DB_HOST=db

   This instructs your ETL container to connect to the PostgreSQL container (named "db" in docker-compose.yml). When running locally via main.py, use "localhost".

   Using Docker Compose:
   1. Build and start the services:
      
         docker-compose up --build

   2. The PostgreSQL container (service: "db") will run on its internal port 5432. The host port mapping (if set) is used only for external connections.
   3. The ETL container will automatically execute the ETL process, including database setup, extraction, transformation, and loading.

4. Using the Makefile
   -------------------
   You can execute common commands via the provided Makefile. Here are some useful targets:

   - Build the Docker Images:
      
         make build

   - Start All Services:
      
         make up

   - Run the ETL Job Once:
      
         make run

   - View Logs:
      
         make logs

   - Open a PostgreSQL Shell:
      
         make db_shell

   - Stop and Remove Containers and Volumes:
      
         make clean

Summary
-------
CryptoStream is a comprehensive project designed to showcase your data engineering skills. It features:

- A modular Python ETL pipeline.
- Integration with the CoinGecko API for real-time Bitcoin pricing data.
- Automated database setup and data ingestion.
- Containerization and orchestration with Docker and Docker Compose.
- Simplified command execution via a Makefile.

Important Configuration Notes:
- Docker Mode: Set DB_HOST=db in your ".env" file to allow inter-container communication.
- Local Mode: Set DB_HOST=localhost when running directly with "python src/main.py".

This project is ready for deployment.
