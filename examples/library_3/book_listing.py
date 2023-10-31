from dataclasses import dataclass

from examples.library_3.book_info import BookInfo

@dataclass()
class BookListing:
    uid: str
    book_info: BookInfo
    existing_copies_count: int
