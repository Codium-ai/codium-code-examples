from examples.library_3.admin import Admin
from examples.library_3.member import Member
from examples.library_3.librarian import Librarian
from examples.library_3.permissions import UserRole
from examples.library_3.library_factory import make_new_library


class TestLibrary3:
    def setup_method(self):
        self.library, self.root_user = make_new_library("root", "super-secret-root-pass")

    def test_admin_create_new_user(self):
        admin_mgmt = self.library.get_admin_management(self.root_user)
        librarian_created = admin_mgmt.new_user(UserRole.LIBRARIAN, "giles", "watcher-on-the-wall")

        librarian_retrieved = admin_mgmt.get_user_by_username("giles")

        assert librarian_retrieved.uid == librarian_created.uid
