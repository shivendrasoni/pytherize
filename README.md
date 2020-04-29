**To start the program**
`python3 run_rbac_demo.py`

**Overview**
Pytherize is a general purpose authorization library that allows user to perform authorization on different actions.
It is by design simple and yet exhaustive in terms of managing authorization for different actions.

Pytherize uses the concept of *policies* which form a unique pairing between an ACTION and a RESOURCE. 
Multiple policies could be attached to a role, which could be assigned to a user.

While it is created in a DB agnostic fashion, it means that for different databases different helpers which implement 
the BaseInterface correctly have to be used.

Presently, it supports the following databases:

1) SQL databases (uses dataset, which is a wrapper on SQLAlchemy)
2) In-Memory DB of the server itself (not recommended for production use cases) 

Features : 

- Granular roles with policies. Two users with same roles can have different access on the same resource.

    For this I borrowed the ACl concept from how AWS implements its permissions a Role can have multiple policies attached to it.
    Policy is basically a pair mapping of the resource and an action.
    
- ActionType is an entity. It can be extended for different use cases. Each action type has a unique id.

- Grouping : Multiple roles can be grouped together to form a grouped role. This role will have policies from all the member roles.

- Sample extension for role class to make a super role for a super user scenario. He can perform any action as long as that the action itself is valid.

- Hierarchy : Roles can be created in hierarchical fashion. On adding a role as a child to another role, it will inherit all the policies of the parent role.
  
  Do note : Hierarchy is not implemented as inheritance of classes as many Roles of same type can also form parent-child relationships. Also, inheritance is best suited to extend the functionality of an entity not the data within its members.
- Support  for DB like ids or UUId etc. & toggle for simpleids (for demo purpose) 
- Ability to list resources

Directory STRUCTURE
 
 * [core](./core)
   * [RBAC](core/SimpleACL.py)
 * [models](./models)
   * [Action Type](models/ActionTypeModel.py)
   * [Policy Model](./models/PolicyModel.py)
   * [Resource](models/ResourceModel.py)
   * [Role](./models/Role.py)
   * [User](./models/User.py)
 
 * [utils](./utils)
    * [CLI](./utils/cli.py)
    * [ID generator](./utils/IdGenerator.py)
 * [README.md](./README.md)

**Footnotes** 

Future scope : 
- Improve error handling. I have done basic error handling but have not added validations for each & every input.
- Unit test
- better migration
- DB adapter for redis, and other dbs.
- Default roles
