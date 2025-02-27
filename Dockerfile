FROM python:3.9-slim

WORKDIR /app

# Copy the source code and requirements
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Default command to run the main script
CMD ["python", "src/main.py"]
