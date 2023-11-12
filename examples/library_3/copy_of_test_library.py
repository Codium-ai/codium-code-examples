# from examples.library_3.admin import Admin
# from examples.library_3.member import Member
# from examples.library_3.librarian import Librarian
# from examples.library_3.permissions import UserRole
# from examples.library_3.library_factory import make_new_library


# class TestLibrary3:
#     def setup_method(self):
#         self.library, self.root_user = make_new_library("root", "super-secret-root-pass")

#     def test_create_new_user(self):
#         admin_mgmt = self.library.get_admin_management(self.root_user)
#         librarian_created = admin_mgmt.new_user(UserRole.LIBRARIAN, "giles", "watcher-on-the-wall")

#         librarian_retrieved = admin_mgmt.get_user_by_username("giles")

#         assert librarian_retrieved.uid == librarian_created.uid


        


# # def test_borrow_book(library):
# #     user_book_management = library.get_user_book_management(Member("John", "pass1234"))
# #     book = BookListing("Book Title", "Author Name", "2022-01-01", 2)
# #     user_book_management.borrow_book(book, Member("John", "pass1234"))
# #     assert book.available_count == 1

# # root_admin = Admin("root", "rootpass")

# # library = Library(root_admin)

# # global_book_db = GlobalBookDB()
# # library_book_db = LibraryBookDB()
# # book_borrowing_db = BookBorrowingDB()
# # user_book_management = UserBookManagement(library)
# # librarian_book_management = LibrarianBookManagement(library)
# # user_management = UserManagement(library)
# # admin_management = AdminManagement(library)
# # user_db = UserDB()
# # audit_log_db = AuditLogDB()
# # audit_log = AuditLog(library)

# # library.set_librarian_book_management(librarian_book_management)
# # library.set_user_book_management(user_book_management)
# # library.set_user_management(user_management)
# # library.set_admin_management(admin_management)
# # library.set_audit_log(audit_log)

# # test_borrow_book(library)