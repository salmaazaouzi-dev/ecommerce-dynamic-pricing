import os
import sqlite3
from typing import List, Tuple

DB_PATH = os.path.join(os.path.dirname(__file__), "pricing.db")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")


def get_connection():
    """Establishes and returns a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initializes the database using schema.sql."""
    if not os.path.exists(SCHEMA_PATH):
        raise FileNotFoundError(f"Schema file not found at {SCHEMA_PATH}")

    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    with get_connection() as conn:
        conn.executescript(schema_sql)
        conn.commit()


def insert_competitor_prices(records: List[Tuple[int, str, float, bool]]):
    """
    Inserts a list of competitor price records into the database.
    Each tuple should contain: (product_id, competitor_name, scraped_price, is_available)
    """
    query = """
    INSERT INTO competitor_prices (product_id, competitor_name, scraped_price, is_available)
    VALUES (?, ?, ?, ?)
    """
    with get_connection() as conn:
        conn.executemany(query, records)
        conn.commit()


if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
