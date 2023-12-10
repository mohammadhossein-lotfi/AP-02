class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = '{} {}'.format(self.firstname, self.lastname)
        self.email = '{}.{}@company.com'.format(self.firstname, self.lastname).lower()