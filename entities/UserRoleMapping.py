import time
from core.ElementTypes import ElementTypes


class UserRoleMapping:
    id = None
    user_id = None
    role_id = None
    created_on = None
    doc_type = ElementTypes.USER_ROLE_MAPPING

    # Add validation decorator
    def __init__(self, user_id=None, role_id=None, id=None, created_on=time.time()):
        self.user_id = user_id
        self.role_id = role_id
        self.id = id
        self.created_on = created_on

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'role_id': self.role_id,
            'created_on': self.created_on
        }
