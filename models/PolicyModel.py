
from models.BaseModel import BaseModel


#Entities imports

from entities.Role import Role
from entities.PolicyResourceActionMapping import PolicyResourceActionMapping
from entities.Policy import Policy
from entities.PolicyRoleMapping import PolicyRoleMapping

from core.ElementTypes import ElementTypes


class PolicyModel(BaseModel):
    doc_type = ElementTypes.POLICY

    def __init__(self, db=None):
        BaseModel.__init__(self, db)
        db.migrate_models(self.doc_type)
        db.migrate_models(ElementTypes.POLICY_RESOURCE_ACTION_MAPPING)
        db.migrate_models(ElementTypes.POLICY_ROLE_MAPPING)

    def find_policy_by_action_and_resource_id(self, resource_id=None, action_id=None)-> PolicyResourceActionMapping:
        fields = {
            'resource_id': [resource_id],
            'action_id': [action_id]
        }
        result = self.db.get_element_by_fields(ElementTypes.POLICY_RESOURCE_ACTION_MAPPING, fields)
        return PolicyResourceActionMapping(**result)

    def find_policy_ids_by_roles(self, roles: [Role])->{str}:
        fields = {
            'role_id': [role.id for role in roles]
        }

        results = self.db.get_elements_by_fields(ElementTypes.POLICY_ROLE_MAPPING, fields)

        policy_ids = set(map(lambda policy_role_mapping: PolicyRoleMapping(**policy_role_mapping).policy_id, results))

        return policy_ids

    def save(self, policy: Policy):
            created_policy = self.db.insert_element_in_db(ElementTypes.POLICY, policy)
            policy_resource_action_mapping = PolicyResourceActionMapping(policy_id=created_policy.id,
                                                                         resource_id=created_policy.resource_id,
                                                                         action_id=created_policy.action_id)
            self.db.insert_element_in_db(ElementTypes.POLICY_RESOURCE_ACTION_MAPPING, policy_resource_action_mapping)


    def get_by_id(self, policy_id):
        policy = self.db.get_element_by_id(ElementTypes.POLICY, policy_id)
        return Policy(**policy)
