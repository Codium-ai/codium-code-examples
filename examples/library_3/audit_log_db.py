class AuditLogDB:
    def __init__(self):
        self.audit_logs = []

    def add_audit_log(self, action, user):
        self.audit_logs.append((action, user))
