
class CLI:
    def __init__(self, rbac):
        self.rbac = rbac

    def add_user(self, name):
        self.rbac.add_user(name)
        print("Added '{}'".format(name))

    def create_role(self, name, desc, type):
        self.rbac.create_role(name, description=desc, type=type)

    def delete_role(self, role_id):
        self.rbac.delete_role(role_id)

    def add_role_to_user(self, user_id, role_id):
        user = self.rbac.get_user_by_id(user_id)
        role = self.rbac.roles[role_id]
        user.add_role(role)

    def add_resource(self, resource_name):
        self.rbac.add_resource(resource_name)

    def create_action(self, action_type):
        self.rbac.create_action(action_type)

    def create_policy(self, action, resource):
        self.rbac.create_policy(action, resource)

    def attach_policy(self, policy, role):
        self.rbac.add_policy_to_role(policy, role)

    def do_group_roles(self, role_name, role_ids):
        roles_to_group = [self.rbac.roles[role_id] for role_id in role_ids]
        self.rbac.group_roles(role_name, roles_to_group, "Grouped Role")

    def can_wrapper(self, user_id, resource_id, action_id):
        return self.rbac.can(user_id, resource_id, action_id)

    @staticmethod
    def display_menu():
        print("Select One of the options below:\n")
        print("#. Run Query")
        print("0. : List entities ")
        print("1. Add User")
        print("2. Create Role")
        print("3. Delete Role")
        print("4. Add Role to User")
        print("5. Create Resource")
        print("6. Create new Action Type [defaults -> READ, WRITE, DELETE] ")
        print("7. Create new policy")
        print("8. Attach policy to role")
        print("9. Group multiple roles together, can also be used to extend an existing role")

    def cmd_loop(self):
        while(True):
            print('Enter * to display menu')
            option = input()
            try:
                if option == '1':
                    self.print_title('Add User')
                    print('Enter Name')
                    name = input()
                    self.add_user(name)
                elif option == '2':
                    self.print_title('Add role')
                    print('Role Name ?')
                    name = input()
                    print('Description if any?')
                    desc = input()
                    print('Type of Role "regular" \n "super"')
                    type = input()

                    self.create_role(name, desc, type)
                elif option == '3':
                    print('Role Id to delete ?')
                    role_id = input()
                    self.delete_role(role_id)

                elif option == '4':
                    self.print_title('Add role to user')
                    print('User id of user?')
                    user_id = input()
                    print('Role id of role')
                    role_id = input()

                    self.add_role_to_user(user_id, role_id)

                elif option == '5':
                    self.print_title('Create Resource')
                    resource_name = input()
                    self.add_resource(resource_name)

                elif option == '6':
                    self.print_title('Create New Action')
                    print('Action Type ?')
                    action_type = input()
                    self.create_action(action_type)

                elif option == '7':
                    self.print_title('Create New Policy')
                    print('Action type id?')
                    action_type_id = input()
                    action_type = self.rbac.actions[action_type_id]
                    print('Resource id ?')
                    resource_id = input()
                    resource = self.rbac.resources[resource_id]
                    self.create_policy(action_type, resource)

                elif option == '8':
                    self.print_title('Attach Policy to Role')
                    print('Policy Id ?')
                    policy_id = input()
                    policy = self.rbac.policies[policy_id]

                    print('Role id?')
                    role_id = input()
                    role = self.rbac.roles[role_id]
                    self.attach_policy(policy, role)
                elif option == '9':
                    self.print_title('Group Multiple Roles')
                    print('Role name ?')
                    name = input()
                    print('Enter comma seperated role ids')
                    role_ids = input().replace(' ', '').split(',')
                    self.do_group_roles(name, role_ids)
                elif option == '#':
                    self.print_title('Run Query')
                    print('Enter query as "user_id,resource_id,action_type_id"')
                    query = input().replace(' ', '').split(',')
                    user_id = query[0]
                    resource_id = query[1]
                    action_type_id = query[2]
                    print('Evaluating if {} can perform {} on {}'.format(user_id, action_type_id, resource_id))
                    query_response = self.can_wrapper(user_id, resource_id, action_type_id)
                    print(query_response)
                elif option == '*':
                    self.display_menu()
                elif option == "0":
                    self.print_title('List all entities of a type')
                    print('Entity type? Options users,policies,resources,roles,actions')
                    entity_type = input()
                    command = 'print(self.rbac.{})'.format(entity_type)
                    eval(command)
                elif option == 'exit':
                    break
            except Exception as e:
                print('An error has occurred')
                print(e)
                continue

    @staticmethod
    def print_title(title):
        print(title)
        print('---------------------------------')


roles = {}
users = {}
policy_roles_map = {}
policies = {}
actions = {}
policy_query_map = {}
resources = {}
