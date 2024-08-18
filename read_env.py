import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
import logging

# Load environment variables from the .env file
load_dotenv()

# Setup logging
logging.basicConfig(
    filename='database_connection.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Read environment variables
database_host = os.getenv('DATABASE_HOST')
database_port = os.getenv('DATABASE_PORT')
database_name = os.getenv('DATABASE_NAME')
database_user = os.getenv('DATABASE_USER')
database_password = os.getenv('DATABASE_PASSWORD')
debug_mode = os.getenv('DEBUG')


# Sample usage
def connect_to_database():
    """Connect to the MySQL database using environment variables."""
    connection = None  # Initialize the connection variable
    cursor = None

    try:
        logging.info('Attempting to connect to the database...')
        connection = mysql.connector.connect(
            host=database_host,
            port=database_port,
            database=database_name,
            user=database_user,
            password=database_password
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            logging.info(f"Connected to MySQL database... MySQL Server version on {db_info}")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            logging.info(f"You're connected to database: {record}")
    except Error as e:
        logging.error(f'error while connecting database:{e}')

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            logging.info('Mysql connection is closed')


if __name__ == "__main__":
    if debug_mode == 'True':
        logging.info("Debug mode is enabled.")
    connect_to_database()
