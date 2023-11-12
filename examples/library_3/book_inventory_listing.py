from dataclasses import dataclass

from examples.library_3.book_info import BookInfo

@dataclass()
class BookInventoryListing:
    """
    The listing inside the inventory, that doesn't change as we borrow books.
    """
    uid: str
    book_info: BookInfo
    existing_copies_count: int
