run:
	uvicorn server:app --reload

requirements-install:
	@pip3 install -r requirements.txt

create-db:
	docker pull postgres
	docker run --name t10 -e POSTGRES_PASSWORD=123 -d -p 5432:5432 postgres

postgres:
	docker exec -it t10 bash
	psql -U postgres
	CREATE DATABASE t10db;