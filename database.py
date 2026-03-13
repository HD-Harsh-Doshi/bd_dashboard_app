import streamlit as st
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# Use the 'Pooled connection' string from Neon (the one with '-pooler')
# This is stored in Streamlit Cloud Secrets
DB_URL = st.secrets["connections"]["neon"]["url"]

def get_connection():
    """Returns a PEP 249 connection object."""
    try:
        return psycopg2.connect(DB_URL)
    except Exception as e:
        st.error(f"Database Connection Error: {e}")
        return None

def get_engine():
    """Returns a SQLAlchemy engine for pandas integration."""
    # Append sslmode if not present (Neon requires SSL)
    url = DB_URL
    if "sslmode" not in url:
        url += "?sslmode=require"
    return create_engine(url)

def load_data():
    """Efficiently loads all donor data into a DataFrame."""
    try:
        engine = get_engine()
        return pd.read_sql("SELECT * FROM donors", engine)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

def run_query(query, params=None):
    """Executes Write/Update/Delete operations."""
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute(query, params)
                conn.commit()
            return True
        except Exception as e:
            st.error(f"Query Error: {e}")
            return False
        finally:
            conn.close()
    return False