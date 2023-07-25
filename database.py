import sqlite3

class JokeDatabase:
    def __init__(self, db_name="jokes.db"):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS jokes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    joke TEXT
                )
            """)
            conn.commit()

    def insert_joke(self, joke):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO jokes (joke) VALUES (?)", (joke,))
            conn.commit()

    def get_jokes(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT joke FROM jokes")
            jokes = cursor.fetchall()
            return [joke[0] for joke in jokes]
