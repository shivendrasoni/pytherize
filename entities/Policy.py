from core.ElementTypes import ElementTypes
from entities.BaseEntity import BaseEntity

class Policy(BaseEntity):
    action_id = None
    resource_id = None
    doc_type = ElementTypes.POLICY

    def __init__(self, name=None, description="", action_id=None, resource_id=None, id=None, created_on=None):
        BaseEntity.__init__(self, name=name, description=description, id=id, created_on=created_on)
        self.action_id = action_id
        self.resource_id = resource_id

    def __str__(self):
        return 'id : {}, action_id: {}, resource_id: {}\n'.format(self.id, self.action_id, self.resource_id)
