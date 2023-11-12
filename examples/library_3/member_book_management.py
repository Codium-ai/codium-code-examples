from examples.library_3.book_listing import BookListing


class MemberBookManagement:
    def __init__(
        self,
        acting_user,
        library_book_db,
        book_borrowing_db,
        ):
        self._acting_user = acting_user
        self._library_book_db = library_book_db
        self._book_borrowing_db = book_borrowing_db

    def find_books(self, author=None, title=None):
        inventory_books = self._library_book_db.find_books(author, title)
    
    def listing_for_inventory_listing(self, book_inventory_listing):
        book_id = book_inventory_listing.uid
        active_borrows = self._book_borrowing_db.get_active_borrows(book_id)
        available_copies_count = book_inventory_listing.existing_copies_count - len(active_borrows)

        return BookListing(
            uid=book_inventory_listing.uid,
            book_info=book_inventory_listing.book_info,
            existing_copies_count=book_inventory_listing.existing_copies_count,
            available_copies_count=available_copies_count,
        )

    def borrow_book(self, book_id):
        book_listing = self._library_book_db.find_book_by_id(book_id)
        active_borrows = self._book_borrowing_db.get_active_borrows(book_id)

        if book_listing.existing_copies_count - len(active_borrows) <= 0:
            raise ValueError("There are no copies of this book available for borrowing")
        return self._book_borrowing_db.borrow(book_listing.uid, self._acting_user.uid)

    def return_book(self, book, user):
        # Return a book
        pass
