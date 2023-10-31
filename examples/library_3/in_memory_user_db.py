from examples.library_3.admin import Admin
from examples.library_3.member import Member
from examples.library_3.librarian import Librarian
from examples.library_3.permissions import UserRole

class InMemoryUserDB:
    def __init__(self, root_user):
        self._user_id_to_user = {
            root_user.uid: root_user,
        }
        self._next_uid = root_user.uid + 1

    def new_user(self, role, username, password):
        user = self._mk_new_user(role, username, password)
        self._user_id_to_user[user.uid] = user
        return user
    
    def _mk_new_user(self, role, username, password):
        for user in self._user_id_to_user.values():
            if user.username == username:
                raise ValueError(f"Username {username} is already exists")
        if role == UserRole.ADMIN:
            return Admin(self._get_next_user_id(), username, password)
        elif role == UserRole.MEMBER:
            return Member(self._get_next_user_id(), username, password)
        elif role == UserRole.LIBRARIAN:
            return Librarian(self._get_next_user_id(), username, password)
        else:
            raise ValueError(f"Unknown role: {role}")
    
    def _get_next_user_id(self):
        uid = self._next_uid
        self._next_uid += 1
        return uid

    def remove_user(self, uid):
        self._user_id_to_user.pop(uid)
    
    def get_user(self, uid):
        return self._user_id_to_user.get(uid)
    
    def get_user_by_username(self, username):
        for user in self._user_id_to_user.values():
            if user.username == username:
                return user
        return None
    
    def get_user_by_username_and_password(self, username, password):
        for user in self._user_id_to_user.values():
            if user.username == username and user.password == password:
                return user
        return None


    # def update_user(self, user):
    #     # Update user info
    #     pass
