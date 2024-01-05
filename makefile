run:
	docker-compose up --build

down:
	docker-compose down

shell:
	docker-compose exec app bash

test:
	docker-compose exec -T app pytest

db_test:
	docker-compose exec -T db psql -U postgres -c "CREATE DATABASE test_db;"

db_init:
	alembic init alembic

db_migrate:
	alembic revision --autogenerate -m "$(NAME)"

db_upgrade:
	alembic upgrade head

rv:
	docker volume rm mc_menu_data_viewer_mc_menu_db_data
