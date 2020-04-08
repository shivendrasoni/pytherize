import time
from core.ElementTypes import ElementTypes


class PolicyRoleMapping:
    id = None
    policy_id = None
    role_id = None
    created_on = None
    doc_type = ElementTypes.POLICY_ROLE_MAPPING

    # Add validation decorator
    def __init__(self, policy_id=None, role_id=None, id=None, created_on=time.time()):
        self.policy_id = policy_id
        self.role_id = role_id
        self.created_on = created_on
        self.id = id

    def __str__(self):
        return 'doc_type: {}, policy_id: {} , role_id: {}\n'.format(self.doc_type,self.policy_id, self.role_id)

    def to_dict(self):
        return {
            'policy_id': self.policy_id,
            'role_id' : self.role_id,
            'created_on': self.created_on
        }
