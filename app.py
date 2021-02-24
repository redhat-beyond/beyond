#!/usr/bin/env python
import mariadb
from beyond import app

config = {
    'host': 'mariadb',
    'port': 3306,
    'user': 'root',
    'password': 'beyond',
    'database': 'beyond'
}

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    conn = mariadb.connect(**config)
