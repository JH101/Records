# Jamie Hilton
# 30/01/15
# student_module_thing


class ModuleTable:
    def __init__(self):
        self.name = None
        self.module1 = None
        self.module2 = None
        self.module3 = None
        self.module4 = None
        self.total = None 

students = []

for record in range(5):
    student = ModuleTable()
    student.name = input("Please enter the name of the student: ")
    student.module1 = int(input("Please enter the students mark for the first module: "))
    student.module2 = int(input("Please enter the students mark for the second module: "))
    student.module3 = int(input("Please enter the students mark for the third module: "))
    student.module4 = int(input("Please enter the students mark for the fourth module: "))
    student.total = (student.module1 + student.module2 + student.module3 + student.module4)
    students.append(student)

print("|Name|Module1|Module2|Module3|Module4|Total|")
for student in students:
    
    print("|{0}|{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>3}{11:>3}".format(student.name,"|", student.module1,"|", student.module2,"|", student.module3,"|", student.module4,"|", student.total, "|"))
    
