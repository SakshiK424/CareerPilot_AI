import sqlite3


DATABASE_NAME = "career_guidance.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def save_resume_analysis(analysis):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO resume_analysis (analysis) VALUES (?)",
        (analysis,)
    )

    conn.commit()
    conn.close()


def save_skill_gap(report):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO skill_gap (report) VALUES (?)",
        (report,)
    )

    conn.commit()
    conn.close()


def save_roadmap(roadmap):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO roadmap (roadmap) VALUES (?)",
        (roadmap,)
    )

    conn.commit()
    conn.close()


def save_market_analysis(report):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO market_analysis (report) VALUES (?)",
        (report,)
    )

    conn.commit()
    conn.close()