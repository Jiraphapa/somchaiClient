import connector
from models import user
from views import login


class Controller:

    def __init__(self):
        self.connector = connector()
        self.user = user.User()