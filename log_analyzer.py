#!/usr/bin/env python3

import psycopg2


conn = psycopg2.connect(dbname="news")
cur = conn.cursor()
cur.execute('''
    SELECT * FROM authors;
''')
