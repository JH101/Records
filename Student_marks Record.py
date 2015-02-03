# Jamie Hilton
# 23/01/2015
# StudentMarkthing

class studentrecord:
    def __init__(self):
        self.name = None
        self.mark = None

records = []

for student in range(3):
    new_record = studentrecord()
    new_record.name = input("Please enter the students name: ")
    new_record.mark = input("Please enter the students mark: ")
    records.append(new_record)

print("-"*31)
print("|{0:<10} {1:>20}|".format("Name", "Mark"))

for student in records:
    print("|{0:<10} {1:>20}|".format(student.name, student.mark))

print("-"*31)
