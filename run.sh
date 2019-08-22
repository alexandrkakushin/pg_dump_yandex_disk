#!/bin/bash

BASEDIR=$(dirname $0)
echo "Script location: ${BASEDIR}"
cd ${BASEDIR}

python3 pg_dump_yandex_disk.py