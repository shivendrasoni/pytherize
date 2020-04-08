from entities.BaseEntity import BaseEntity
from core.ElementTypes import ElementTypes
import time

class User(BaseEntity):
    doc_type = ElementTypes.USER
    id = None

    def __init__(self, name=None, description=None, id=None, created_on=None):
        BaseEntity.__init__(self, name=name, description=description, id=id, created_on=created_on)

    def __str__(self):
        return 'id : {}, name: {}\n'.format(self.id, self.name)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_on': self.created_on,
            'description': self.description
        }
