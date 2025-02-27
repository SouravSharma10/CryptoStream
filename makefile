.PHONY: build up down logs restart db_shell clean

run:
	python src/main.py

# Build all services defined in docker-compose.yml
build:
	docker-compose build

# Start all services
up:
	docker-compose up

# Stop and remove all containers (but preserve volumes)
down:
	docker-compose down

# Follow logs from all services
logs:
	docker-compose logs -f

# Restart services (down then up)
restart: down up

# Open a psql shell on the PostgreSQL container
db_shell:
	docker-compose exec db psql -U postgres -d crypto_db

# Stop all services and remove containers and volumes
clean:
	docker-compose down -v
