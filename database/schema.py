import sqlite3


def initialize_database():

    conn = sqlite3.connect("career_guidance.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resume_analysis(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        analysis TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS skill_gap(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        report TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS roadmap(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roadmap TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS market_analysis(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        report TEXT
    )
    """)

    conn.commit()
    conn.close()