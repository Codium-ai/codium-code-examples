class LibrarianBookManagement:
    def __init__(self,
        library_book_db,
        book_borrowing_db,
        ):
        self._library_book_db = library_book_db
        self._book_borrowing_db = book_borrowing_db

    def add_book(self, book_listing):
        self._library_book_db.add_book(book_listing)


    def find_books(self, author=None, title=None):
        # Find books by author, title or both
        return self._library_book_db.find_books(author, title)

    def borrow_book(self, book, user):
        # Borrow a book on behalf of a user
        pass

    def return_book(self, book, user):
        # Return a book on behalf of a user
        pass
