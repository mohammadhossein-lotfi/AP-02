class Employee:
	def __init__(self, fullname, **kwargs):
		self.name = fullname.split()[0]
		self.lastname = fullname.split()[1]
		for attr, val in kwargs.items():
			exec('self.{} = val'.format(attr))