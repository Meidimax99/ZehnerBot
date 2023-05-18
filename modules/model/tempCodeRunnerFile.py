def load_users() -> list:
    with open('data/users.json', 'r') as json_file:
        data_users = json.load(json_file)
        return data_users