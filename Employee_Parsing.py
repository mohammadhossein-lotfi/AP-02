class Employee:
	def __init__(self, firstname, lastname, salary):
		self.firstname = firstname
		self.lastname = lastname
		self.salary = int(salary)
		
	def from_string(string):
		x = string.split('-')
		return Employee(x[0], x[1], int(x[2]))