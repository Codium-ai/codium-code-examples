from examples.library_3.admin import Admin
from examples.library_3.library import Library3
from examples.library_3.in_memory_user_db import InMemoryUserDB
from examples.library_3.admin_management_factory import AdminManagementFactory


def make_new_library(root_username, root_password):
    root_user = Admin(1, root_username, root_password)

    user_db = InMemoryUserDB(root_user)
    admin_management_factory = AdminManagementFactory(user_db)

    library = Library3(admin_management_factory)
    return library, root_user
