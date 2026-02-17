# Improved Database

import sqlite3
import logging

class Database:
    def __init__(self, db_file):
        """Connect to the SQLite database specified by db_file."""
        self.connection = None
        try:
            self.connection = sqlite3.connect(db_file)
        except sqlite3.Error as e:
            logging.error(f"Error connecting to database: {e}")
            raise

    def execute_query(self, query, params=None):
        """Execute a single query."""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as e:
            logging.error(f"Error executing query: {e}")
            raise
        finally:
            cursor.close()

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            logging.info("Database connection closed.")
        else:
            logging.warning("No connection to close.")

# Usage example; This should be removed in production:
# db = Database('example.db')
# db.execute_query('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
# db.close_connection()