from conf import Conf
from yandex_disk import YandexDisk
from pg import Pg
import datetime


def run():
    conf = Conf()
    if not conf.valid:
        print('quit')
        quit()

    yadisk = YandexDisk(conf.yandex)
    pg = Pg(conf.pg)

    # Создание каталога с дампами
    yadisk.mkdir(conf.yandex.dir)

    # Создание каталога YYYY-mm
    dir_dumps = conf.yandex.dir + "/%s" % datetime.datetime.now().strftime('%Y-%m')
    yadisk.mkdir(dir_dumps)

    file_name = '/tmp/pg_dump_yandex_disk.sql.tar'
    # Создание дампа
    pg.dump(file_name)

    yadisk.upload(file_name, "%s/%s.sql.tar" %
                  (dir_dumps, datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')))


run()
