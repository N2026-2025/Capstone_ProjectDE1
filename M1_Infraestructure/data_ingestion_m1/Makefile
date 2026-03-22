up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker build -t tickets_ingest:v1 .

ingest:
	docker run -it \
	--network=$(shell docker network ls | grep _default | awk '{print $2}') \
	tickets_ingest:v1

logs:
	docker-compose logs -f
