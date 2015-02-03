# Jamie Hilton
# 30/01/15
# Pay Slip Printer

class pay_slip:
    def __init__(self):
        self.name = None
        self.employee_number = None
        self.hours = None
        self.rate = None

print("Pay Slip Generator")

employee = pay_slip()

employee.name = input("Please enter the name of the employee: ")
employee.employee_number = int(input("Please enter the employee's number: "))
employee.hours = int(input("Please enter the hours worked by this employee: "))
employee.rate = float(input("Please enter the hourly rate of pay: £"))

print("*"*30)
print("* Pay Slip {0:>19}".format("*"))
print("* {0:>28}".format("*"))
print("* Name: {0} {1:>13}".format(employee.name, "*"))
print("* Employee Number: {0} {1:>4}".format(employee.employee_number, "*"))
print("* Hours Worked: {0} {1:>11}".format(employee.hours, "*"))
print("* Rate of Pay: £{0} {1:>9}".format(employee.rate, "*"))
print("* {0:>28}".format("*"))
print("* Total Pay: £{0:.2f} {1:>10}".format((employee.hours*employee.rate), "*"))
print("*"*30)
