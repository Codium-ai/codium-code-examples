from examples.library_3.librarian_book_management import LibrarianBookManagement


class LibrarianBookManagementFactory:
    def __init__(
            self,
            library_book_db,
            book_borrowing_db,
            ):
        self._library_book_db = library_book_db
        self._book_borrowing_db = book_borrowing_db
    
    def get_librarian_book_management(self, acting_user):
        return LibrarianBookManagement(
            acting_user=acting_user,
            library_book_db=self._library_book_db,
            book_borrowing_db=self._book_borrowing_db,
            )
