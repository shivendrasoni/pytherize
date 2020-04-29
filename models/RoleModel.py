from models.BaseModel import BaseModel

# Entities imports

from entities.Role import Role
from entities.Policy import Policy
from entities.PolicyRoleMapping import PolicyRoleMapping

from core.ElementTypes import ElementTypes


class RoleModel(BaseModel):
    doc_type = ElementTypes.ROLE

    def __init__(self, db):
        BaseModel.__init__(self, db)
        self.policies = []

    def get_by_id(self, role_id) -> 'Role':
        fetched_role = self.db.get_element_by_id(self.doc_type, role_id)
        return Role(**fetched_role)

    def create_policy_role_mapping(self, role: Role, policy: Policy):
        mapping = PolicyRoleMapping(role_id=role.id, policy_id=policy.id)
        return self.db.insert_element_in_db(ElementTypes.POLICY_ROLE_MAPPING, mapping)

    def create_policy_role_mapping_bulk(self, role: Role, policy_ids:[str]):
        mappings = [PolicyRoleMapping(role_id=role.id, policy_id=policy_id) for policy_id in policy_ids]

        self.db.insert_element_in_db_bulk(ElementTypes.POLICY_ROLE_MAPPING, mappings)

    def remove_policy_role_mapping_by_policy(self, role: Role, policy: Policy):
        fields = {
            'policy_id': policy.id,
            'role_id': role.id
        }

        return self.db.delete_by_query(ElementTypes.POLICY_ROLE_MAPPING, fields)

    def remove_policy_role_mapping_by_role(self, role_id):
        fields = {
            'role_id': role_id
        }
        self.db.delete_by_query(ElementTypes.POLICY_ROLE_MAPPING, fields)

    # Needs to be authenticated itself
    def delete_role(self, role):
        self.db.remove_element_by_id(self.doc_type, role.id)
        self.remove_policy_role_mapping_by_role(role.id)

    def find_roles_by_policy(self, policy_id: str) -> [Role]:
        role_ids = self.find_roles_ids_by_policy(policy_id=policy_id)
        roles = self.db.get_element_by_id_bulk(ElementTypes.ROLE, role_ids)
        return [Role(**role) for role in roles]

    def find_roles_ids_by_policy(self, policy_id: str) -> [Role]:
        fields = {
            'policy_id': policy_id
        }
        role_policy_mappings = self.db.get_elements_by_fields(doc_type=ElementTypes.POLICY_ROLE_MAPPING, fields=fields)

        role_ids = [role_id['role_id'] for role_id in role_policy_mappings]
        return role_ids

    def save(self, role: Role):
        created_role = self.db.insert_element_in_db(self.doc_type, role)
        return created_role

    def remove(self, role: Role):
        pass
