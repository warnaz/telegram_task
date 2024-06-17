# funnel-bot-exercise

## How to start:

1. Create and fill up the `.env` file, example is `.env.example`
2. Install python3.11+
3. Run `pip install -r requirements.txt`
4. Run `alembic upgrade head` to create db tables
5. Run `python main.py` to start the script
6. Log into the telegram account using phone + code

## Docs:

- Messages can be changed at `config/messages.py`
- Used libraries
    ```
    Pyrogram==2.0.106        # Telegram Client
    SQLAlchemy==2.0.30       # ORM & data models
    asyncpg==0.29.0          # Postgres Async Engine
    pydantic-settings==2.3.3 # To read .env
    alembic==1.13.1          # Manage DB migrations
    ```
- Project structure
    ```
    ├── README.md
    ├── alembic.ini
    ├── configs
    │   └── messages.py
    ├── main.py
    ├── migrations
    │   ├── README
    │   ├── env.py
    │   ├── script.py.mako
    │   └── versions
    │       └── 2024-06-17_initial.py
    ├── requirements.txt
    └── src
        ├── __init__.py
        ├── core
        │   ├── __init__.py
        │   ├── config.py
        │   └── loader.py
        ├── database
        │   ├── __init__.py
        │   ├── database.py
        │   └── models
        │       ├── __init__.py
        │       ├── base.py
        │       └── user.py
        ├── handlers.py
        └── services
            ├── __init__.py
            ├── funnel.py
            └── users.py
    ```
