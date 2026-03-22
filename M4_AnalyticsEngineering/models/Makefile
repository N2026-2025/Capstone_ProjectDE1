.PHONY: setup run test

setup:
	pip install dbt-postgres apache-flink kafka-python
	docker-compose pull

run:
	docker-compose up -d
	@echo "Esperando servicios..."
	sleep 15
	dbt run --project-dir dbt_project

test:
	dbt test --project-dir dbt_project

alert:
	@echo "Configurando Webhooks de Slack para fallos de Pipeline..."
