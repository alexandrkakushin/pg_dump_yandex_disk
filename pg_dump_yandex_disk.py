from conf import Conf
from yandex_disk import YandexDisk
from pg import Pg


def run():
    conf = Conf()
    if not conf.valid:
        print('quit')
        quit()

    yadisk = YandexDisk(conf.yandex)
    pg = Pg(conf.pg)

    # Создание каталога с дампами
    yadisk.mkdir(conf.yandex.dir)

    file_name = '/tmp/pg_dump_yandex_disk.sql.tar'
    # Создание дампа
    pg.dump(file_name)


run()
