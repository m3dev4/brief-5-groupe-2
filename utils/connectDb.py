from mysql.connector import Error
from dotenv import load_dotenv
import os



load_dotenv()  # Load environment variables from .env file

secret_key = os.getenv(
    "PASSWORD_DB"
)  # Get the value of PASSWORD_DB from environment variables


def connect_db():
    import mysql.connector
    try:
        my_db = mysql.connector.connect(
            host="localhost", user="root", password=secret_key, database="my_store"
        )

        if my_db.is_connected():
            print("Connexion à la base de données réussie!")
            return my_db
    except Error as e:
        print(f"Erreur lors de la connexion à la base de données: {e}")
        return None
