run:
	docker-compose up --build

down:
	docker-compose down

format:
	black .

db_init:
	alembic init alembic

db_migrate:
	alembic revision --autogenerate -m "$(NAME)"

db_upgrade:
	alembic upgrade head

rv:
	docker volume rm mc_menu_data_viewer_mc_menu_db_data
