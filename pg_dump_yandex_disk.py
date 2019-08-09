from conf import Conf
from yandex_disk import YandexDisk


def run():
    conf = Conf()
    if not conf.valid:
        print('quit')
        quit()

    yadisk = YandexDisk(conf.yandex)

    # Создание каталога с дампами
    yadisk.mkdir(conf.yandex.dir)


run()
