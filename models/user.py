class User:
    def __init__(self):
        self.firstName = ''
        self.lastName = ''
        self.email = ''
        self.privillege = ''

    def setUser(self, firstName, lastName, email, privillege='normal'):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.privillege = privillege

class Manager(User):
    def __init__(self):

