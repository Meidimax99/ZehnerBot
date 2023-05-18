from modules.model.user import user


class user_list:
    users: user = []

    def __init__(self):
        self.data = []

    def add_user(self, name: str, proof: str, day_list=[]):
        new_user: user = user.create(name, proof, day_list)
        self.users.append(new_user)

    def print_user_list(self):
        print(self.users)


def main():
    print("test")


main()
