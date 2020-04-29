from core.ElementTypes import *
import dataset
import random
import string

class SQLDB():

    table_refs = {}

    def __init__(self):
        user_name = 'cWSOmNfhPO'
        password = '6OSxoyXUPP'
        db_name = 'cWSOmNfhPO'
        host = 'remotemysql.com'
        db_url = 'mysql+mysqlconnector://{}:{}@{}/{}'.format(user_name, password, host, db_name)
        self.db = dataset.connect(db_url)
        self.run_migrations()

    @staticmethod
    def get_id_(prefix):
        return prefix + '_' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

    def get_element_by_id(self, doc_type: ElementTypes, id:str):
        table_name = doc_type.value
        return self.table_refs[table_name].find_one(id=id)

    def get_element_by_id_bulk(self, doc_type:ElementTypes, ids:[str]):
        table_name = doc_type.value
        return list(self.table_refs[table_name].find(id=ids))

    def update_element_by_id(self, doc_type: ElementTypes, element:object):
        data = element.__dict__
        table_name = doc_type.value
        self.table_refs[table_name].update(data, ['id'], ensure=True)
        return element

    def insert_element_in_db(self, doc_type: ElementTypes, element: object):
        resp = self.insert_element_in_db_bulk(doc_type, [element])
        return resp[0]

    def insert_element_in_db_bulk(self, doc_type:str, elements:[object]):
        table_name = doc_type.value
        for element in elements:
            element.id = self.get_id_(table_name)

        rows = [element.to_dict() for element in elements]
        try:
            self.table_refs[table_name].insert_many(rows, ensure=True)
            return elements
        except Exception as e:
            raise e

    def remove_element_by_id(self, doc_type:ElementTypes, doc_id):

        query = {
            'id': doc_id
        }
        self.delete_by_query(doc_type, query)

    # Returns a generator
    def list_elements(self, doc_type: ElementTypes):
        table_name = doc_type.value
        for item in self.table_refs[table_name].all():
            print(item)

    def delete_by_query(self, doc_type: str, fields: dict):
        if not fields:
            return
        table_name = doc_type.value
        return self.table_refs[table_name].delete(**fields)

    def update_by_query(self):
        pass

    def get_elements_by_fields(self, doc_type: ElementTypes, fields, limit=10):

        table_name = doc_type.value
        return list(self.table_refs[table_name].find(**fields, _limit=limit))

    def get_element_by_fields(self, doc_type: ElementTypes, fields:dict) -> ElementTypes:
        return self.get_elements_by_fields(doc_type, fields)[0]

    def migrate_models(self, doc_type):
        table_name = doc_type.value
        table_ref = self.db.create_table(table_name, primary_type=self.db.types.string(30))
        self.table_refs[table_name] = table_ref

    def run_migrations(self):
        for doc_type in ElementTypes:
            self.migrate_models(doc_type=doc_type)

