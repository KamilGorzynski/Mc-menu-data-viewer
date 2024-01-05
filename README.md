# MC-MENU-DATA-VIEWER

## Stack:
- Python
- Flask
- Alembic
- Postgres
- Docker

## Requirements:
- docker-compose

## Installation:
I. Clone the project:
```
https://github.com/KamilGorzynski/Mc-menu-data-viewer.git
```

II. Create .env.local file and fill up with example variables:
```
FLASK_ENV=development
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=mc_menu_db
DATABASE_URL=postgresql://postgres:postgres@db:5432/mc_menu_db
```

III. Run app:
```
make run
```

## Own Migrations
After make a changes in models run:
```
make db_migrate NAME='my_migration_name'
make db_upgrade
```

## Run unit tests
To create db for unit tests (run once):
```
make db_test
```

Run unit tests:
```
make test
```

## Code Format
Run black with default settings (not ready yet):
```
make format
```
