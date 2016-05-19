class Reservation:
    def __init__(self):
        self.topic = ''
        self.room = ''
        self.start = ''
        self.end = ''
        self.owner = ''

    def setReservation(self, topic, room, start, end, owner):
        self.topic = topic
        self.room = room
        self.start = start
        self.end = end
        self.owner = owner

    def get_topic(self):
        return self.topic

    def get_room(self):
        return self.room

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def get_owner(self):
        return self.owner