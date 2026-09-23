import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path

DB_PATH = Path("data/trips.db")

st.title("OBD Telematics Dashboard")

# Connect to SQLite database
conn = sqlite3.connect(DB_PATH)
df = pd.read_sql_query("SELECT * FROM readings", conn)
st.dataframe(df)
conn.close()