from enum import Enum
import json
from os import path


class verified_status (Enum):
    uncertain = 0
    on_time = 1
    too_late = 2
    excuse = 3


class User:

    def __init__(self, user_id: int, username: str, name: str, verified: bool, proof: str, day_list={}):
        self.path = 'data/users.json'
        self.user_id = user_id
        self.username: str = username
        self.name: str = name
        self.verified: bool = verified
        self.proof: str = proof
        if len(day_list) == 0:
            self.day_list = {"Monday": 0,
                             "Tuesday": 0,
                             "Wednesday": 0,
                             "Thursday": 0,
                             "Friday": 0,
                             "Saturday": 0,
                             "Sunday": 0}
        else:
            self.day_list = day_list

    def update_verified_status(self, verified: bool, proof: str):
        self.verified = verified
        self.proof = proof

    def add_day_to_list(self, day: str):
        self.day_list[day] = 1

    def delete_day_from_list(self, day: str):
        self.day_list[day] = 0

    def print_day_list(self):
        print(self.day_list)

    def print_user_info(self):
        print(self.name, self.username, "hat sich an den Tagen ", self.day_list, "eingetragen.\n",
              "Vertrag unterschrieben?", self.verified, "Proof: ", self.proof)

    def save_user(self):
        data_users = load_users()
        old_user = find_user(self.name)
        if len(old_user) != 0:
            data_users.remove(old_user)
        listObj = {"user_id": self.user_id, "name": self.name, "username": self.username, "day_list": self.day_list,
                   "verified": self.verified, "proof": self.proof}
        data_users.append(listObj)

        if path.isfile(self.path) is False:
            raise Exception("File not found, please ask Paul Müller for help")
        with open(self.path, 'w') as json_file:
            json.dump(data_users, json_file,
                      indent=4,
                      separators=(',', ': '))


def find_user(name: str) -> dict:
    data_users = load_users()
    for i in data_users:
        if i["name"] == name:
            return i
        else:
            return {}


def dict_to_user(dict: dict) -> User:
    print("\n", dict["name"])
    user = User(dict["user_id"], dict["username"],
                dict["name"], dict["verified"], dict["proof"], dict["day_list"])
    return user


def load_users() -> list:
    with open('data/users.json', 'r') as json_file:
        data_users = json.load(json_file)
        return data_users


# leo = User(12345, "Kampf.Tomate", "Leonhard", True, "123", {
#     "Monday": 1,
#     "Tuesday": 1,
#     "Wednesday": 0,
#     "Thursday": 0,
#     "Friday": 0,
#     "Saturday": 0,
#     "Sunday": 0
# })
# print(type(leo))
# leo_dict = find_user("Leonhard")
# print(leo_dict)
# leo = dict_to_user(leo_dict)
# leo.print_day_list()
# leo.add_day_to_list("Wednesday")
# leo.print_day_list()
# leo.save_user()
