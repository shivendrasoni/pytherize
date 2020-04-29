from core.SimpleACL import SimpleACL
from utils.SQLDatabaseUtils import SQLDB

if __name__ == "__main__":
    db = SQLDB()
    rbac = SimpleACL(db)

    # user_request = dict(name='Nistha', country='India', description='pagal guy')
    # user = rbac.add_user(user_request)

    # fetched_user = rbac.get_user_by_id(user.id)
    #
    # print(fetched_user)
    # #
    #
    # # ROLE 1
    # role_request = dict(name='Admin', description='descrption demo', type = 'regular')
    # role_1 = rbac.create_role(role_request)
    #
    #
    #
    # action_request = dict(name='READ', description='allows reading resource')
    # action = rbac.create_action(action_request)
    # # fetch_action = rbac.action_model.get_by_id(action.id)
    #
    # resource_request = dict(name='DB_API', description='')
    # resource = rbac.add_resource(resource_request)
    # # fetch_resource = rbac.resource_model.get_by_id(resource.id)
    #
    # policy_request_1 = dict(name='p1', action=action, resource=resource, description="policy 1 aur kya")
    # policy_1 = rbac.create_policy(policy_request_1)
    # # policy_1 = rbac.policy_model.get_by_id(p1.id)
    # # role_1_by_id = rbac.get_role_by_id(role_1.id)
    # p_r_mapping = rbac.add_policy_to_role(policy=policy_1, role=role_1)
    #
    #
    # # ROLE 2
    #
    # role_request = dict(name='USER', description='2222 demo', type = 'regular')
    # role_2 = rbac.create_role(role_request)
    #
    # # rbac.delete_role(role)
    #
    # action_request = dict(name='WRITE', description='allows2 reading resource')
    # action_2 = rbac.create_action(action_request)
    # # fetch_action = rbac.action_model.get_by_id(action.id)
    #
    # resource_request = dict(name='DB_22API', description='2434324')
    # resource2 = rbac.add_resource(resource_request)
    # # fetch_resource = rbac.resource_model.get_by_id(resource.id)
    #
    # policy_request_2 = dict(name='p2', action=action_2, resource=resource2, description="policy 2 bhaiyo aur behno aur kya")
    # policy_2 = rbac.create_policy(policy_request_2)
    # # policy_1 = rbac.policy_model.get_by_id(p1.id)
    # # role_1_by_id = rbac.get_role_by_id(role_1.id)
    # p_r_mapping = rbac.add_policy_to_role(policy=policy_2, role=role_2)
    #
    # # group_role = rbac.group_roles(name='parivar_role', roles=[role_2, role_1])
    #
    # # rbac.delete_role(group_role)
    #
    # rbac.add_role_to_user(user=user, role=role_1)
    # print(user)

    fetched_user = rbac.user_model.get_by_id('user_9ON')
    action_2 = rbac.action_model.get_by_id('action_7JE')

    fetch_resource = rbac.resource_model.get_by_id('resource_WH2')
    print(rbac.can(user=fetched_user, action=action_2, resource=fetch_resource))
