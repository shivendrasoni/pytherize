from core.ElementTypes import ElementTypes
from entities.BaseEntity import BaseEntity
from dataclasses import dataclass, asdict, field, InitVar

@dataclass
class ActionType(BaseEntity):
    doc_type = ElementTypes.ACTION

    def __init__(self, name, description, id=None, created_on=None):
        BaseEntity.__init__(self, name=name, description=description, id=id, created_on=created_on)

    def __str__(self):
        return 'id : {}, name: {}\n'.format(self.id, self.name)


if __name__ == '__main__':
    action = ActionType('READ', 'reads')
    print(action)
