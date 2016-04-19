class User:
    def __init__(self):
        self.firstName = ''
        self.lastName = ''
        self.email = ''

    def setUser(self, firstName, lastName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email