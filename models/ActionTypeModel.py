from models.BaseModel import BaseModel
from entities.ActionType import ActionType
from core.ElementTypes import ElementTypes


class ActionTypeModel(BaseModel):
    doc_type = ElementTypes.ACTION

    def __init__(self, db):
        BaseModel.__init__(self, db)
        db.migrate_models(self.doc_type)

    def save(self, action: ActionType):
        return self.db.insert_element_in_db(self.doc_type, action)

    def get_by_id(self, action_id: str):
        action = self.db.get_element_by_id(self.doc_type, action_id)
        return ActionType(**action)
