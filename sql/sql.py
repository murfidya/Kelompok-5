import sqlite3

conn = sqlite3.connect("hospital_project.db")
cursor = conn.cursor()

with open("sql/hospital_project.sql", "r") as f:
    sql_script = f.read()

cursor.executescript(sql_script)
conn.commit()
conn.close()
