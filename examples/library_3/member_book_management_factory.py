from examples.library_3.member_book_management import MemberBookManagement


class MemberBookManagementFactory:
    def __init__(
            self,
            library_book_db,
            book_borrowing_db,
            ):
        self._library_book_db = library_book_db
        self._book_borrowing_db = book_borrowing_db
    
    def get_member_book_management(self, acting_user):
        return MemberBookManagement(
            acting_user=acting_user,
            library_book_db=self._library_book_db,
            book_borrowing_db=self._book_borrowing_db,
            )
