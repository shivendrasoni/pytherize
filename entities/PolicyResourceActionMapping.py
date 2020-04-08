import time
from core.ElementTypes import ElementTypes


class PolicyResourceActionMapping:
    id = None
    policy_id = None
    role_id = None
    created_on = None
    doc_type = ElementTypes.POLICY_RESOURCE_ACTION_MAPPING

    # Add validation decorato

    def __init__(self, id=None, policy_id=None, resource_id=None, action_id=None, created_on=time.time()):
        self.id = id
        self.policy_id = policy_id
        self.resource_id = resource_id
        self.action_id = action_id
        self.created_on = created_on

    def __str__(self):
        return 'id : {}, policy_id: {} , action_id: {}, resource_id: {}\n'.format(self.id, self.policy_id, self.action_id, self.resource_id)

    def to_dict(self):

        return {
            'policy_id': self.policy_id,
            'resource_id' : self.resource_id,
            'action_id' : self.action_id,
            'created_on': self.created_on
        }
