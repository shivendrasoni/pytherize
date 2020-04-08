# Model imports
from models.BaseModel import BaseModel

# Entities imports

from entities.User import User
from entities.Role import Role
from entities.UserRoleMapping import UserRoleMapping

from core.ElementTypes import ElementTypes
from utils.SQLDatabaseUtils import SQLDB


class UserModel(BaseModel):
    country = None
    roles = []
    doc_type = ElementTypes.USER

    def __init__(self, db: SQLDB=None):
        BaseModel.__init__(self, db)
        db.migrate_models(self.doc_type)
        db.migrate_models(ElementTypes.USER_ROLE_MAPPING)

    def save(self, user: User):
        saved_user = self.db.insert_element_in_db(self.doc_type, user)
        return saved_user

    def get_by_id(self, user_id):
        fetched_user = self.db.get_element_by_id(self.doc_type, user_id)
        return User(**fetched_user)

    def add_role(self, role: Role, user: User):
        mapping = UserRoleMapping(user_id=user.id, role_id=role.id)
        return self.db.insert_element_in_db(ElementTypes.USER_ROLE_MAPPING, mapping)

    def add_roles_bulk(self, roles: [Role], user: User):
        mappings = [UserRoleMapping(role_id=role.id, user_id=user.id) for role in roles]
        self.db.insert_element_in_db_bulk(ElementTypes.USER_ROLE_MAPPING, mappings)

    def get_user_role_mappings_for_user(self, user: User=None):
        fields = {
            'user_id': user.id
        }

        results = self.db.get_elements_by_fields(doc_type=ElementTypes.USER_ROLE_MAPPING, fields=fields)

        return [UserRoleMapping(**row) for row in results]



