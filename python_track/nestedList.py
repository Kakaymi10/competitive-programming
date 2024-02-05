n = int(input())
student_grades = []
grades = []
for i in range(n):
    name=input()
    mark=float(input())
    student_grades.append([name, mark])
    grades.append(mark)

grades = sorted(set(grades))
second_lowest = grades[1]
names = []
for student in student_grades:
    if student[1] == second_lowest:
        names.append(student[0])

names.sort()

for name in names:
    print(name)
           
