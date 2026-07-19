import sqlite3
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("SELECT count(*) FROM users")
#cursor.execute("PRAGMA table_info(expenses)")
#id,expense,amount,date,user_id,category
print(cursor.fetchall())

conn.close()
