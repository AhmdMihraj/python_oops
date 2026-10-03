import sqlite3
 
# Create/connect to database
conn = sqlite3.connect("tution.db")
 
# Create a cursor
cursor = conn.cursor()
 
# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        fullname TEXT,
        age INTEGER,
        mobile_number TEXT,
        email_address TEXT,
        password TEXT,
        date_of_birth TEXT,
        gender TEXT,
        preferred_language TEXT,
        school_college_name TEXT,
        class_grade TEXT,
        board_curriculum TEXT,
        academic_year integer ,
        tuition_subjects TEXT,
        current_level_by_subject TEXT
    )
""")

# Save changes
conn.commit()
 
# Close connection
conn.close()
 
print("Database created successfully!")