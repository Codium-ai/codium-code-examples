from examples.library_3.admin import Admin
from examples.library_3.librarian_book_management_factory import LibrarianBookManagementFactory
from examples.library_3.library_3 import Library3
from examples.library_3.in_memory_user_db import InMemoryUserDB
from examples.library_3.admin_management_factory import AdminManagementFactory
from examples.library_3.librarian_book_management import LibrarianBookManagement
from examples.library_3.member_book_management import MemberBookManagement
from examples.library_3.in_memory_library_book_db import InMemoryLibraryBookDB
from examples.library_3.book_borrowing_db import BookBorrowingDB
from examples.library_3.member_book_management_factory import MemberBookManagementFactory


def make_new_library(root_username, root_password):
    root_user = Admin(1, root_username, root_password)

    user_db = InMemoryUserDB(root_user)
    admin_management_factory = AdminManagementFactory(user_db)

    book_db = InMemoryLibraryBookDB()
    borrowing_db = BookBorrowingDB()

    librarian_book_management_factory = LibrarianBookManagementFactory(
        library_book_db=book_db,
        book_borrowing_db=borrowing_db,
    )

    member_book_management_factory = MemberBookManagementFactory(
        library_book_db=book_db,
        book_borrowing_db=borrowing_db,
    )

    library = Library3(
        librarian_book_management_factory=librarian_book_management_factory,
        member_book_management_factory=member_book_management_factory,
        admin_management_factory=admin_management_factory,
        )
    return library, root_user
