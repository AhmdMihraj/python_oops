#this file is to test all functionlity inside student classs1
#in future this class will be used to real senerio


from modules.student.student import studentclass


#student registraion

email=input("enter your email")
password = input("  ter your password")

s1=studentclass()
s1.usernameandpassword(email,password)