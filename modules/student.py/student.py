class studentclass:
    def __init__(self):
        self.name = ""
        self.fullname = ""
        self.date_of_birth = ""
        self.age = ""
        self.gender = ""
        self.mobile_number = ""
        self.email_address = ""
        self.preferred_language = ""
        self.school_college_name = ""
        self.class_grade = ""
        self.board_curriculum = ""
        self.academic_year = ""
        self.tuition_subjects = []
        self.current_level_by_subject = {}
        self.areas_of_help = []

        # Parent/guardian details (for minors)
        self.parent_guardian_name = ""
        self.relationship_with_student = ""
        self.parent_mobile_number = ""
        self.parent_email_address = ""
        self.preferred_communication_method = ""

    def __str__(self):
        return (
            f"Student: {self.fullname or self.name}, DOB: {self.date_of_birth}, "
            f"Age: {self.age}, Gender: {self.gender}, Mobile: {self.mobile_number}, "
            f"Email: {self.email_address}, Language: {self.preferred_language}"
        )
    