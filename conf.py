import json


class Conf():

    def __init__(self):
        self.conf_file = 'conf.json'
        self.data = self.load()
        self.check(self.data)

    def load(self):
        with open(self.conf_file) as json_file:
            data = json.load(json_file)
            return data

    def check(self, data):
        print('Checking settings:')
        try:
            print(' Yandex.Disk : ', end='')
            self.check_yandex_disk(data)
        except Exception as ex:
            print("FAIL (" + str(ex) + ")")
        else:
            print("OK")

        try:
            print(' PostgreSQL  : ', end='')
            self.check_postgres(data)
        except Exception as ex:
            print("FAIL (" + str(ex) + ")")
        else:
            print("OK")

    def check_yandex_disk(self, data):
        if 'yandex' in data:
            if 'login' not in data['yandex']:
                raise ValueError(
                    'No key "login" in setting Yandex.Disk connection')
            if 'password' not in data['yandex']:
                raise ValueError(
                    'No key "password" in setting Yandex.Disk connection')
        else:
            raise ValueError('No key YANDEX in conf')

    def check_postgres(self, data):
        if 'pg' in data:
            if 'host' not in data['pg']:
                raise ValueError('No key "host" in setting DB connection')
            if 'db' not in data['pg']:
                raise ValueError('No key "db" in setting DB connection')
            if 'login' not in data['pg']:
                raise ValueError('No key "login" in setting DB connection')
            if 'password' not in data['pg']:
                raise ValueError('No key "password" in setting DB connection')
