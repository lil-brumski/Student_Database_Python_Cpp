import build.Student as Student


#Instantiates an object called 'studentInfo'
studentInfo = Student.Database()

#Takes the user's name.
name = input("Enter your name: ")

#Takes the user's no. of O'level credits.
o_level_credits = int(input("Enter the number of credits you had in your O\'level exam: "))

#Takes the user's age.
age = int(input("Enter your age: "))

#Takes JAMB score.
JAMB = int(input("Enter your JAMB score: "))

#Takes Post UTME score.
POST_UTME = int(input("Enter your POST UTME score: "))

#A method that checks if a student us qualified.
studentInfo.checkStudent(name, o_level_credits, age, JAMB, POST_UTME)

#Gives qualified student admission.
studentInfo.admission()

#Prints the admitted students' details to an external file.
studentInfo.admissionList()