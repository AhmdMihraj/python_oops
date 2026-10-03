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

cursor.execute("""
INSERT INTO students VALUES (
        001,
        'mihraj',
        'Ahmd Mihraj',
        19,
        7592848759,
        'mihrajmj3@gmail.com',
        'mj@123',
        '2007-06-01',
        'male',
        'english',
        'Ilahia college of arts and science',
        'A',
        'computer science',
        '2025-2028',
        'c,python,java',
        'beginner,beginner,beginner',
        'non'
    )
""")
# Save changes
conn.commit()
 
# Close connection
conn.close()
 
print("Database created successfully!")