from examples.library_3.user import User


class Librarian(User):
    def __init__(self, uid, username, password):
        super().__init__(uid, username, password)
