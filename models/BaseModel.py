

class BaseModel:
    db = None
    doc_type = None

    def __init__(self, db=None):
        if db is None:
            raise Exception('Database access object : None')
        self.db = db

    def list_elements(self):
        self.db.list_elements(self.doc_type)
