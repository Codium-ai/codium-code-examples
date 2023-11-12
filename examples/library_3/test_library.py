from examples.library_3.admin import Admin
from examples.library_3.book_info import BookInfo
from examples.library_3.book_inventory_listing import BookInventoryListing
from examples.library_3.book_listing import BookListing
from examples.library_3.member import Member
from examples.library_3.librarian import Librarian
from examples.library_3.permissions import UserRole
from examples.library_3.library_factory import make_new_library


class TestLibrary3:
    def setup_method(self):
        self.library, self.root_user = make_new_library("root", "super-secret-root-pass")

    def test_admin_can_create_new_librarian_user(self):
        admin_mgmt = self.library.get_admin_management(self.root_user)
        librarian_created = admin_mgmt.new_user(UserRole.LIBRARIAN, "Giles", "watcher-on-the-wall")

        librarian_retrieved = admin_mgmt.get_user_by_username("Giles")

        assert librarian_retrieved.uid == librarian_created.uid

    def test_admin_can_delete_user(self):
        admin_mgmt = self.library.get_admin_management(self.root_user)
        librarian_created = admin_mgmt.new_user(UserRole.LIBRARIAN, "Giles", "watcher-on-the-wall")

        # Verify the user exists
        librarian_retrieved = admin_mgmt.get_user_by_username("Giles")
        assert librarian_retrieved.uid == librarian_created.uid

        admin_mgmt.delete_user(librarian_created.uid)
        librarian_retrieved_after_delete = admin_mgmt.get_user_by_username("Giles")
        assert librarian_retrieved_after_delete is None
    
    def test_librarian_can_add_books(self):
        admin_mgmt = self.library.get_admin_management(self.root_user)
        librarian = admin_mgmt.new_user(UserRole.LIBRARIAN, "Giles", "watcher-on-the-wall")

        librarian_book_mgmt = self.library.get_librarian_book_management(librarian)

        book_info = BookInfo(
            uid="book-info-uid-1",
            author="Dracula",
            title="Yummy Humans",
            )
        book_listing = BookInventoryListing(
            uid="book-listing-uid-1",
            book_info=book_info,
            existing_copies_count=3,
            )
        librarian_book_mgmt.add_book(book_listing)

        book_listing_retrieved = librarian_book_mgmt.find_books(author="Dracula")
        assert book_listing_retrieved == [book_listing]

    
    def test_user_can_borrow_book(self):
        admin_mgmt = self.library.get_admin_management(self.root_user)
        librarian = admin_mgmt.new_user(UserRole.LIBRARIAN, "Giles", "watcher-on-the-wall")
        member = admin_mgmt.new_user(UserRole.MEMBER, "Willow", "its-magic")

        librarian_book_mgmt = self.library.get_librarian_book_management(librarian)

        book_info = BookInfo(
            uid="book-info-uid-1",
            author="Dracula",
            title="Yummy Humans",
            )
        book_listing = BookInventoryListing(
            uid="book-listing-uid-1",
            book_info=book_info,
            existing_copies_count=3,
            )
        librarian_book_mgmt.add_book(book_listing)

        member_book_mgmt = self.library.get_member_book_management(member)

        borrow = member_book_mgmt.borrow_book(book_listing.uid)

        assert borrow is not None


        


        
