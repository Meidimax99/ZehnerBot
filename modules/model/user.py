from enum import Enum


class verified_status (Enum):
    uncertain = 0
    on_time = 1
    too_late = 2
    excuse = 3


class user:
    name: str
    verified: verified_status
    proof: str
    day_list = []

    def create(self, name: str, proof: str, day_list=[]):
        self.name = name
        self.verified = verified_status.uncertain
        self.proof = proof
        day_list = day_list
