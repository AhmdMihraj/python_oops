class studentclass:
    def __init__(self):
        self.name = ""
        self.fullname = ""
        self.date_of_birth = ""
        self.age = ""
        self.gender = ""
        self.mobile_number = ""
        self.email_address = ""
        self.password = ""
        self.preferred_language = ""
        self.school_college_name = ""
        self.class_grade = ""
        self.board_curriculum = ""
        self.academic_year = ""

        # Parent/guardian details (for minors)
        self.parent_guardian_name = ""
        self.relationship_with_student = ""
        self.parent_mobile_number = ""
        self.parent_email_address = ""
        self.preferred_communication_method = ""

    
    def usernameandpassword(self,email,password):
        self.email_address = email
        self.password = password


    def studentdetails(self,mobile_number,fullname,date_of_birth,gender,preferred_language,school_college_name,class_grade,board_curriculum,academic_year):
           
        self.mobile_number = mobile_number  
        self.fullname = fullname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.preferred_language = preferred_language
        self.school_college_name = school_college_name
        self.class_grade = class_grade
        self.board_curriculum = board_curriculum
        self.academic_year = academic_year


    def savetoDB(self):
        import sqlite3
        conn = sqlite3.connect("tution.db")
        cursor = conn.cursor()     
        cursor.execute(""" 
                INSERT INTO students (
                    name,
                    fullname,
                    age,
                    mobile_number,
                    email_address,
                    password,
                    date_of_birth,
                    gender,
                    preferred_language,
                    school_college_name,
                    class_grade,
                    board_curriculum,
                    academic_year
                    
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                self.name,
                self.fullname,
                self.age,
                self.mobile_number,
                self.email_address,
                self.password,
                self.date_of_birth,
                self.gender,
                self.preferred_language,
                self.school_college_name,
                self.class_grade,
                self.board_curriculum,
                self.academic_year
            ))

        # Save changes and close connection
        conn.commit()
        conn.close()