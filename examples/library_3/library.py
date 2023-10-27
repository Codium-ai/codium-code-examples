from examples.library_3.permissions import (
    is_admin,
    is_librarian,
    is_member,
    )


class Library3:
    def __init__(
            self,
            # librarian_book_management,
            # user_book_management,
            # user_management,
            admin_management_factory,
            # audit_log,
            ):
        # self.librarian_book_management = None
        # self.user_book_management = None
        # self.user_management = None
        self._admin_management_factory = admin_management_factory
        # self.audit_log = None
    
    # def get_librarian_book_management(self, user):
    #     if is_admin(user) or user.is_librarian():
    #         return self.librarian_book_management
    #     else:
    #         raise Exception("User is not authorized to access LibrarianBookManagement")

    # def get_user_book_management(self, user):
    #     if user.is_member():
    #         return self.user_book_management
    #     else:
    #         raise Exception("User is not authorized to access UserBookManagement")

    # def get_user_management(self, user):
    #     if user.is_admin() or user.is_librarian():
    #         return self.user_management
    #     else:
    #         raise Exception("User is not authorized to access UserManagement")

    def get_admin_management(self, user):
        if is_admin(user):
            return self._admin_management_factory.get_admin_management(user)
        else:
            raise Exception("User is not authorized to access AdminManagement")
