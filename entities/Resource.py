from entities.BaseEntity import BaseEntity
from core.ElementTypes import ElementTypes


class Resource(BaseEntity):
    doc_type = ElementTypes.RESOURCE

    def __init__(self, name=None, description=None, id=None, created_on=None):
        BaseEntity.__init__(self, name=name, description=description, id=id, created_on=created_on)

    def __str__(self):
        return 'id : {}, name: {}\n'.format(self.id, self.name)
