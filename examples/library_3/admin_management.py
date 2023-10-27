class AdminManagement:
    def __init__(self, acting_user, user_db):
        self._user_db = user_db
        self._acting_user = acting_user

    def new_user(self, role, username, password):
        return self._user_db.new_user(role, username, password)
    
    def get_user_by_username(self, username):
        return self._user_db.get_user_by_username(username)

    def delete_user(self, user):
        # Delete a user
        pass

    def update_user(self, user):
        # Update user info
        pass

