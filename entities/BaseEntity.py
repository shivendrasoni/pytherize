import time
class BaseEntity:
    id = None
    name = None
    description = None
    created_on = None
    doc_type = None

    # Add validation decorator
    def __init__(self, name, description = "", id=None, created_on=None):
        self.name = name
        self.description = description
        if id:
            self.id = id
        if created_on:
            self.created_on = created_on
        else:
            self.created_on = time.time()

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return vars(self)
