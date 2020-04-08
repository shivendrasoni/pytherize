from models.BaseModel import BaseModel


# Entities imports

from entities.Resource import Resource

from core.ElementTypes import ElementTypes


class ResourceModel(BaseModel):
    doc_type = ElementTypes.RESOURCE

    def __init__(self, db):
        BaseModel.__init__(self, db)
        db.migrate_models(self.doc_type)

    def save(self, resource: Resource):
        return self.db.insert_element_in_db(self.doc_type, resource)

    def get_by_id(self, resource_id):
        resource = self.db.get_element_by_id(self.doc_type, resource_id)
        return Resource(**resource)
