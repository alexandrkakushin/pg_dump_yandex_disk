import json


class Conf():

    def __init__(self):
        self.conf_file = 'conf.json'
        self.data = self.__load()
        self.valid = self.__check(self.data)
        if self.valid:
            self.yandex = Yandex(self.data['yandex'])
            self.pg = Pg(self.data['pg'])

    def __load(self):
        with open(self.conf_file) as json_file:
            data = json.load(json_file)
            return data

    def __check(self, data):
        result = True
        print('Checking settings:')
        try:
            print(' Yandex.Disk : ', end='')
            self.__check_yandex_disk(data)
        except Exception as ex:
            print("FAIL (" + str(ex) + ")")
            result = False
        else:
            print("OK")

        try:
            print(' PostgreSQL  : ', end='')
            self.__check_postgres(data)
        except Exception as ex:
            print("FAIL (" + str(ex) + ")")
            result = False
        else:
            print("OK")
        return result

    def __check_yandex_disk(self, data):
        if 'yandex' in data:
            if 'login' not in data['yandex']:
                raise ValueError(
                    'No key "login" in setting Yandex.Disk connection')
            if 'password' not in data['yandex']:
                raise ValueError(
                    'No key "password" in setting Yandex.Disk connection')
            if 'dir' not in data['yandex']:
                raise ValueError(
                    'No key "dir" in setting Yandex.Disk connection')
        else:
            raise ValueError('No key YANDEX in conf')

    def __check_postgres(self, data):
        if 'pg' in data:
            if 'host' not in data['pg']:
                raise ValueError('No key "host" in setting DB connection')
            if 'db' not in data['pg']:
                raise ValueError('No key "db" in setting DB connection')
            if 'login' not in data['pg']:
                raise ValueError('No key "login" in setting DB connection')
            if 'password' not in data['pg']:
                raise ValueError('No key "password" in setting DB connection')


class Yandex():
    def __init__(self, conf_yandex):
        self.login = conf_yandex['login']
        self.password = conf_yandex['password']
        self.dir = conf_yandex['dir']


class Pg():
    def __init__(self, conf_pg):
        self.host = conf_pg['host']
        self.port = conf_pg['port']
        self.db = conf_pg['db']
        self.login = conf_pg['login']
        self.password = conf_pg['password']
