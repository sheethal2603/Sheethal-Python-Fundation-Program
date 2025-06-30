import mysql.connector
from util.db_property_util import get_property_string

def get_connection():
    db_config = get_property_string("resources/db.properties")
    connection = mysql.connector.connect(**db_config)
    return connection
