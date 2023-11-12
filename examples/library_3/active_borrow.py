from dataclasses import dataclass


@dataclass()
class ActiveBorrow:
    uid: str
    book_id: str
    user_id: str
