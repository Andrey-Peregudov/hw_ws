import datetime
import uuid
from datetime import datetime
from pony.orm import *

from werkzeug.security import check_password_hash

db = Database()


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    username = Required(str, unique=True)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
