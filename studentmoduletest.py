#this file is to test all functionlity inside student classs1
#in future this class will be used to real senerio


from modules.student.student import studentclass


#student registraion

email=input("enter your email")
password = input(" enter your password")

s1=studentclass()
s1.usernameandpassword(email,password)

#student details

phone_number = input("enter your phone number")
fullname = input("enter your full name")
date_of_birth = input("enter your date of birth")
gender = input("enter your gender")
preferred_language = input("enter your preferred language")
school_college_name = input("enter your school/college name")
class_grade = input("enter your class/grade")
board_curriculum = input("enter your board/curriculum")
academic_year = input("enter your academic year")

s1.studentdetails(fullname,date_of_birth,gender,preferred_language,school_college_name,class_grade,board_curriculum,academic_year)