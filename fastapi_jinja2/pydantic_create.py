from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    # address: Optional[str]
    # name: str
    # tel: Optional[str]
    # password: str