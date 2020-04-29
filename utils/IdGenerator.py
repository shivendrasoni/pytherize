import random
import string

class IdGenerator:
    SIMPLE_IDS= None

    def __init__(self, simple_ids=True):
        self.SIMPLE_IDS = simple_ids

    @staticmethod
    def get_id_(prefix):
        return prefix + '_' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
