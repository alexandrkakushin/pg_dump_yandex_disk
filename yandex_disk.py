from requests import request


class YandexDisk():
    def __init__(self, conf_yandex):
        self.login = conf_yandex.login
        self.password = conf_yandex.password

    def __send_request(self, operation, url):
        URL_WEB_DAV = 'https://webdav.yandex.ru'

        headers = {"Accept": "*/*"}
        response = request("MKCOL", URL_WEB_DAV + url, headers=headers,
                           auth=(self.login, self.password))
        return response

    def mkdir(self, path):
        response = self.__send_request("MKCOL", path)
        if response.status_code == 409:
            # TODO: Yandex Disk Exception
            raise OSError("Can not create directory: %s" % path)
