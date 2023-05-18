from enum import Enum


class verified_status (Enum):
    uncertain = 0
    on_time = 1
    too_late = 2
    excuse = 3


class weekdays (Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6


class user:
    def __init__(self, name: str, verified: bool, proof: str, day_list: weekdays = []):
        self.name: str = name
        self.verified: bool = verified
        self.proof: str = proof
        self.day_list = [day_list]

    def update_verified_status(self, verified: bool, proof: str):
        self.verified = verified
        self.proof = proof

    def change_day_list(self, day_list: weekdays = []):
        self. day_list = day_list

    def add_day_to_list(self, weekday: weekdays):
        self.day_list.append(weekday)

    def print_day_list(self):
        print(self.day_list)

    def print_user_info():
        print()


leo = user("leo", True, "123", [weekdays.Monday, weekdays.Friday])
leo.update_verified_status(False, "321")
leo.change_day_list([weekdays.Sunday])
leo.add_day_to_list(weekdays.Thursday)
leo.print_day_list()
