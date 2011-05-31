import os.path

HERE = os.path.abspath(os.path.dirname(__file__))
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(HERE, 'test.db')

INSTALLED_APPS = (
    'modelvalidated',
)

