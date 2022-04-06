#!/bin/bash

FILE_NAME=dump_`date +%Y-%m-%d"_"%H_%M_%S`.sql
BACKUP_DIR=/home/dev/database_backup
pg_dump hirkano_robomech > ${BACKUP_DIR}/${FILE_NAME}
