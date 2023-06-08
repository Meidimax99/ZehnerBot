from dataTable import DataTable
import pickle

class DataStore:
    user_file_str = "data/user"
    days_file_str = "data/days"
    votes_file_str = "data/votes"
    voted_file_str = "data/voted"
    debt_file_str = "data/debt"

    def __init__(self):
        self.user = DataTable(["name", "mo", "di", "mi", "do", "fr", "sa", "so"])
        self.days = DataTable(["user_id", "anwesend?", "entschuldigt?"])
        self.votes = DataTable(["user_id", "date", "votes_for", "votes_against", "end_date"])
        self.voted = DataTable(["voted"])
        self.debt = DataTable(["debtor", "value"])

    def save(self):
        with open(self.user_file_str, "wb") as user_file:
            pickle.dump(self.user, user_file)
        with open(self.days_file_str, "wb") as days_file:
            pickle.dump(self.days, days_file)
        with open(self.votes_file_str, "wb") as votes_file:
            pickle.dump(self.votes, votes_file)
        with open(self.voted_file_str, "wb") as voted_file:
            pickle.dump(self.voted, voted_file)
        with open(self.debt_file_str, "wb") as debt_file:
            pickle.dump(self.debt, debt_file)


    def load(self):
        with open(self.user_file_str, "rb") as user_file:
            self.user = pickle.load(user_file)
        with open(self.days_file_str, "rb") as days_file:
            self.days = pickle.load(days_file)
        with open(self.votes_file_str, "rb") as votes_file:
            self.votes = pickle.load(votes_file)
        with open(self.voted_file_str, "rb") as voted_file:
            self.voted = pickle.load(voted_file)
        with open(self.debt_file_str, "rb") as debt_file:
            self.debt = pickle.load(debt_file)

'''
dataStore = DataStore()
dataStore.user.create({"name": "Paul", "mo":True, "di": False, "mi": True, "do": False, "fr": True, "sa": False, "so": True})
dataStore.user.create({"name": "Pauler", "mo":True, "di": True, "mi": True, "do": False, "fr": True, "sa": False, "so": True})
dataStore.user.create({"name": "am Paulsten", "mo":True, "di": False, "mi": True, "do": False, "fr": True, "sa": False, "so": True})
dataStore.save()

dataStore2 = DataStore()
dataStore2.load()
print(dataStore2.user.filter({"di": False, "mi":True}))
'''