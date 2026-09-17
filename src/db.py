import sqlite3

conn = sqlite3.connect("data/trips.db")

cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS trips (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    start_time TEXT NOT NULL
);""")
cursor.execute("""CREATE TABLE IF NOT EXISTS readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trip_id INTEGER NOT NULL,
    timestamp TEXT NOT NULL,
    pid_name TEXT NOT NULL,
    value REAL NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trips (id)
);""")
conn.commit()

