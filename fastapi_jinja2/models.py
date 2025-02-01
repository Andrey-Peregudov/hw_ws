import datetime
import uuid
from datetime import datetime
from pony.orm import *
from pydantic import validator
from werkzeug.security import generate_password_hash, check_password_hash

db = Database()


class City(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)

    user = Set("User")


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    username = Required(str, unique=True)
    email = Optional(str, unique=True)
    name = Required(str)
    address = Optional(str)
    tel = Optional(str)
    password_hash = Required(str)
    date_reg = Required(datetime, default=lambda: datetime.utcnow())
    last_time = Required(datetime, default=lambda: datetime.utcnow())
    is_active = Required(bool, default=True)

    city = Required(City)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
