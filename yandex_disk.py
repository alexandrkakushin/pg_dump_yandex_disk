from requests import request


class YandexDisk():
    def __init__(self, conf_yandex):
        self.login = conf_yandex.login
        self.password = conf_yandex.password

    def __send_request(self, operation, url, data=None):
        URL_WEB_DAV = 'https://webdav.yandex.ru'

        headers = {"Accept": "*/*"}
        response = request(operation, URL_WEB_DAV + url, headers=headers,
                           auth=(self.login, self.password), data=data)
        return response

    def mkdir(self, path):
        response = self.__send_request("MKCOL", path)
        if response.status_code == 409:
            # TODO: Yandex Disk Exception
            raise OSError("Can not create directory: %s" % path)

    def upload(self, file, path):
        with open(file, "rb") as f:
            resp = self.__send_request("PUT", path, data=f)
            if resp.status_code != 201:
                # TODO: Yandex Disk Exception
                raise OSError("Can not upload file: %s" % file)
