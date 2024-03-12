from dotenv import load_dotenv
import os
from mysql import connector

load_dotenv()

def db_connect():
    config = {
        'user': os.getenv('USER'),
        'password': os.getenv('PASSWORD'),
        'host': os.getenv('HOST'),
        'database': 'breast_cancer_project'
    }
    try:
        return connector.connect(**config)
    except (connector.Error, IOError) as err:
        print(err)
        return None