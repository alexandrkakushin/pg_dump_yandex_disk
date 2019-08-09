from subprocess import PIPE, Popen
import shlex


class Pg():
    def __init__(self, conf_pg):
        self.host = conf_pg.host
        self.port = conf_pg.port
        if self.port == None:
            self.port = 5432

        self.db = conf_pg.db
        self.login = conf_pg.login
        self.password = conf_pg.password

    def dump(self, file_name):
        command = 'PGPASSWORD={0} && export PGPASSWORD && pg_dump -h {1} -d {2} -U {3} -p {4} -Ft -f {5}'\
            .format(
                self.password,
                self.host,
                self.db,
                self.login,
                self.port,
                file_name)
        proc = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        proc.wait()