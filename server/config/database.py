from os import environ
from dotenv import load_dotenv, find_dotenv
from orator import DatabaseManager

load_dotenv(find_dotenv())

DATABASES = {
    'mysql': {
        'driver': 'mysql',
        'host': environ['DB_HOST'],
        'database': environ['DB_NAME'],
        'user': environ['DB_USER'],
        'password': environ['DB_PASSWORD'],
        'prefix': ''
    }
}

db = DatabaseManager(DATABASES)
