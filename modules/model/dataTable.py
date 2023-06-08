import random

class DataTable:
    data = {}
    cols = []

    '''
    Datastructure:
    {
        ID1: {name: "Paul", nickname: "Pelikan", ...}
        ID2: {name: "Christian", ...}
        ...
    }
    
    '''

    def __init__(self, columns):
        self.cols = columns

    def create(self, value_dict, id=None):
        if self.validate_create(value_dict):
            id = self.generate_id() if id==None else id
            self.data[id] = value_dict

    def read(self, id):
        return self.data[id]

    def read_all(self):
        return self.data

    def update(self, id, changes_dict):
        if validate_update(changes_dict) and validate_id(id):
            for key in changes_dict:
                self.data[id][key] = changes_dict[key]

    def delete(self, id):
        if validate_id(id):
            del self.data[id]

    def filter(self, column_value_dict):
        return_dict = {}
        for key in self.data:
            keys_fit = True
            for filter_key in column_value_dict:
                if self.data[key][filter_key] != column_value_dict[filter_key]:
                    keys_fit = False
            if keys_fit:
                return_dict[key] = self.data[key]
        return return_dict

    def validate_id(self, id):
        return id in self.data.keys()

    def validate_create(self, value_dict):
        necessary_keys = set(self.cols)
        given_keys = set(value_dict.keys())
        return necessary_keys == given_keys

    def validate_update(self, changes_dict):
        all_keys = set(self.cols)
        given_keys = set(value_dict.keys())
        return (given_keys - all_keys) == set([])

    def generate_id(self):
        new_id = random.randint(0, 99999)
        while new_id in self.data.keys():
            new_id = random.randint(0, 99999)
        return new_id