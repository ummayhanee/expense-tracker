import sqlite3

conn = sqlite3.connect("expenses.db")

cursor = conn.cursor()


#cursor.execute(""" CREATE TABLE IF NOT EXISTS expenses( id INTEGER PRIMARY KEY AUTOINCREMENT, expense TEXT NOT NULL,  amount REAL NOT NULL,date TEXT NOT NULL) """)
#cursor.execute("ALTER TABLE expenses ADD COLUMN category TEXT")
 # cursor.execute("""CREATE TABLE users ( user_id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL UNIQUE,    email TEXT NOT NULL UNIQUE,    password_hash TEXT NOT NULL)""")

conn.commit()

conn.close()

print("Database created successfully!")

