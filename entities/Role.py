from core.ElementTypes import ElementTypes
from entities.BaseEntity import BaseEntity


class Role(BaseEntity):
    doc_type = ElementTypes.ROLE

    def __init__(self, id=None, name=None, description="", created_on=None, type='regular'):
        BaseEntity.__init__(self, name=name, description=description, id=id, created_on=created_on)
        self.type = type

    def __str__(self):
        return 'id : {}, name: {}, description {}\n'.format(self.id, self.name, self.description)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_on': self.created_on,
            'description': self.description
        }
