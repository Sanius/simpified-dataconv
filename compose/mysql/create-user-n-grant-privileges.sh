#!/bin/bash

set -e
set -u

mysql -u root -p$MYSQL_ROOT_PASSWORD <<-EOSQL
    GRANT ALL PRIVILEGES ON *.* TO '$MYSQL_USER'@'%';
    FLUSH PRIVILEGES;
EOSQL
