#Write Python statements to retrieve the following information from the list stRecord:
#a) Percentage of the student
#b) Marks in the fifth subject
#c) Maximum marks of the student
#d) Roll no. of the student
#e) Change the name of the student from 'Raman' to 'Raghav

stRecord = ['Raman', 'A-36', 56, 98, 99, 72, 69, 78.8]
print("percentage of the student",78.8)
print("marks in the fifth subject",69)
print("maximum marks of the student",99)
print("roll no. of the student",'A-36')
for i in stRecord:
    if i == 'Raman':
        print("Raghav")
