from examples.library_3.active_borrow import ActiveBorrow


class BookBorrowingDB:
    def __init__(self):
        self._active_borrows = {}
        self._next_uid = 1
    
    def _get_next_user_id(self):
        uid = self._next_uid
        self._next_uid += 1
        return uid

    def borrow(self, book_id, user_id):
        active_borrow = ActiveBorrow(
            self._get_next_user_id(),
            book_id,
            user_id,
            )
        self._active_borrows[active_borrow.uid] = active_borrow
        return active_borrow

    def return_book(self, book_id, user):
        for borrow in self._active_borrows.values():
            if borrow.book_id == book_id and borrow.user_id == user.uid:
                self._active_borrows.pop(borrow.uid)
        else:
            raise ValueError(f"Book with UID {book_id} is not borrowed by user {user.uid}")
