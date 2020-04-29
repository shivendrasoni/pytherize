# Models import

from models.ResourceModel import ResourceModel
from models.RoleModel import RoleModel
from models.ActionTypeModel import ActionTypeModel
from models.PolicyModel import PolicyModel
from models.UserModel import UserModel


#Entities imports

from entities.User import User
from entities.Role import Role
from entities.ActionType import ActionType
from entities.Resource import Resource
from entities.Policy import Policy
from entities.PolicyResourceActionMapping import PolicyResourceActionMapping

from core.ElementTypes import ElementTypes
from utils.SQLDatabaseUtils import SQLDB


class SimpleACL:
    # element_types
    def __init__(self, db:SQLDB):

        self.user_model = UserModel(db)
        self.role_model = RoleModel(db)
        self.action_model = ActionTypeModel(db)
        self.resource_model = ResourceModel(db)
        self.policy_model = PolicyModel(db)


    def can(self, user:User=None, resource:Resource=None, action:ActionType=None):
        """
        Tells if a user(user_id) CAN perform an action (action_id) ON a resource(resource_id)
        :param user_id:
        :param resource_id:
        :param action_id:
        :return: bool
        """
        # Get all roles attained by the user
        user_role_mappings = self.user_model.get_user_role_mappings_for_user(user=user)

        user_role_ids = set([user_role.role_id for user_role in user_role_mappings])

        policy_action_resource_mapping = self.policy_model.find_policy_by_action_and_resource_id(resource_id=resource.id
                                                                                                 , action_id=action.id)
        policy_id = policy_action_resource_mapping.policy_id
        # For the current policy find all role ids which have this policy attached
        roles_ids_with_current_policy = set(self.role_model.find_roles_ids_by_policy(policy_id=policy_id))

        # if there is an intersection between the roles user has and the roles with this policy attached, user CAN
        # perform the operation
        roles_intersection = user_role_ids.intersection(roles_ids_with_current_policy)

        return len(roles_intersection) > 0

    ####################
    #  USER OPERATIONS
    ####################

    def add_user(self, user_request):
        name = user_request['name']
        description = user_request['description']
        user = User(name=name, description=description)
        created_user = self.user_model.save(user)

        return created_user

    def get_user_by_id(self, user_id):
        return self.user_model.get_by_id(user_id)

    def add_role_to_user(self, role:Role=None, user:User=None):
        return self.user_model.add_role(role=role, user=user)

    ####################
    # ROLE OPERATIONS
    ####################

    def get_role_by_id(self, role_id):
        return self.role_model.get_by_id(role_id)

    def create_role(self, role_request):
        role_name = role_request['name']
        description = role_request['description']
        role_type = None
        if 'type' in role_request:
            role_type = role_request['type']

        role = None
        if role_type == 'regular' or role_type == '' or role_type is None:
            role = Role(name=role_name, description=description, type=role_type)

        created_role = self.role_model.save(role)
        return created_role

    def delete_role(self, role: Role):
        self.role_model.delete_role(role)

    def add_policy_to_role(self, policy: Policy=None, role: Role=None):
        return self.role_model.create_policy_role_mapping(role, policy)

    def remove_policy_from_role(self, policy: Policy=None, role: Role=None):
        return self.role_model.remove_policy_role_mapping_by_policy(role, policy)

    def get_role_by_policy(self, policy: Policy=None)-> [Role]:
        return self.role_model.find_roles_by_policy(policy.id)

    def group_roles(self, name=None, roles: [Role]=None, description="Grouped Role"):
        grouped_role = Role(name=name, description=description)

        grouped_role = self.role_model.save(grouped_role)
        policy_ids = self.policy_model.find_policy_ids_by_roles(roles)

        self.role_model.create_policy_role_mapping_bulk(grouped_role, policy_ids)
        return grouped_role

    ####################
    # ACTION OPERATIONS
    ####################

    def create_action(self, action_type_request):
        action_name = action_type_request['name']
        description = action_type_request['description']
        action = ActionType(name=action_name, description=description)

        return self.action_model.save(action)

    ####################
    # RESOURCE OPERATIONS
    ####################

    def add_resource(self, resource_request):
        resource_name = resource_request['name']
        description = resource_request['description']
        resource = Resource(name=resource_name, description=description)
        return self.resource_model.save(resource)

    ####################
    # POLICY OPERATIONS
    ####################

    def create_policy(self, policy_request):
        action_id = policy_request['action'].id
        resource_id = policy_request['resource'].id
        name = policy_request['name']
        description = policy_request['description']

        policy = Policy(name=name, description=description, action_id=action_id, resource_id=resource_id)
        self.policy_model.save(policy)
        return policy
