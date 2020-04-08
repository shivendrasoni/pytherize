from enum import Enum

class ElementTypes(Enum):
    USER = 'user'
    ACTION = 'action'
    POLICY = 'policy'
    RESOURCE = 'resource'
    ROLE = 'role'
    POLICY_RESOURCE_ACTION_MAPPING = 'policy_resource_action_mapping'
    POLICY_ROLE_MAPPING = 'policy_role_mapping'
    USER_ROLE_MAPPING = 'user_role_mapping'
