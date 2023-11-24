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

II. Run app:
```
make run
```

## Own Migrations
After make a changes in models run:
```
make db_migrate NAME='my_migration_name'
make db_upgrade
```

