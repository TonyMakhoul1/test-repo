class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    # dunder init mathod esma (__ hole hene l dunder)
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("Tony", "Makho", 50000)
emp_2 = Employee("Tarek", "Faour", 60000)

# print(emp_1)
# 3mlt method l repr em 3atane nfs l output tb3 l repr bl print emp_1
# abel ma a3mil __str__ bas 3mlt str byaatine l output metla


"""
print(repr(emp_1))
print(str(emp_1))


print(emp_1.__repr__())
print(emp_1.__str__())
# the same output aand l fo2
"""

print(emp_1 + emp_2)
# he men l __add__ method li 3mlta
# ana elet eno bas ejma3 2 object men hal class yjma3 l salary

print(len('test'))
print('test'.__len__())
# hole l tnen the same

print(len(emp_1))
# hon ana 3mlt method jdide ela 3tita ta3tine l len tb3 l fullname
