import build.Student as Student

studentInfo = Student.Database()

name = input("Enter your name: ")

o_level_credits = int(input("Enter the number of credits you had in your O\'level exam: "))

age = int(input("Enter your age: "))

JAMB = int(input("Enter your JAMB score: "))

POST_UTME = int(input("Enter your POST UTME score: "))

studentInfo.checkStudent(name, o_level_credits, age, JAMB, POST_UTME)

studentInfo.admission()

studentInfo.admissionList()