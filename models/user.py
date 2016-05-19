from . import Reservation, TodoList

class User:
    def __init__(self):
        self.firstName = ''
        self.lastName = ''
        self.email = ''
        self.phone = ''
        self.privillege = ''
        self.department = ''

    def setUser(self, firstName, lastName, email, phone, privillege='normal', department='None'):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.privillege = privillege
        self.department = department

    def get_fullName(self):
        return self.get_firstName() + " " + self.get_lastName()


    def get_firstName(self):
        return self.firstName

    def get_lastName(self):
        return self.lastName

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_privillege(self):
        return self.privillege

    def get_department(self):
        return self.department

    def create_reservation(self,topic, room, start, end):
        r = Reservation.Reservation()
        r.setReservation(topic, room, start, end, self)
        return r

    def order(self, description, a):
        t = TodoList.TodoList()
        t.set_TodoList(description, a)
        return t

    def __str__(self):
        return self.get_fullName() + " " + self.email + " " + self.get_phone() + " " + self.get_department() + " " + self.get_privillege()


