from examples.library_3.admin_management import AdminManagement


class AdminManagementFactory:
    def __init__(self, user_db):
        self._user_db = user_db
    
    def get_admin_management(self, user):
        return AdminManagement(user, self._user_db)
