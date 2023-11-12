from examples.library_3.admin import Admin
from examples.library_3.member import Member
from examples.library_3.librarian import Librarian


def is_admin(user):
    return isinstance(user, Admin)

def is_member(user):
    return isinstance(user, Member)

def is_librarian(user):
    return isinstance(user, Librarian)

class UserRole:
    MEMBER = "member"
    LIBRARIAN = "librarian"
    ADMIN = "admin"
