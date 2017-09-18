#!/usr/bin/env python3

import psycopg2

# Create psycopg2 connection and curor objects
conn = psycopg2.connect(dbname="news")
cur = conn.cursor()

# Query for most popular articles
cur.execute('''
    SELECT articles.title, COUNT(title) AS Views
    FROM log
    LEFT JOIN articles ON log.path LIKE '%' || articles.slug || '%'
    WHERE status='200 OK' AND title IS NOT NULL
    GROUP BY articles.title
    ORDER BY COUNT(title) DESC
    LIMIT 3;
''')

topArticles = cur.fetchall()

# Query for most popular authors
cur.execute('''
    SELECT authors.name, COUNT(name) AS Views
    FROM authors
    RIGHT JOIN articles ON authors.id = articles.author
    RIGHT JOIN log ON log.path LIKE '%' || articles.slug || '%'
    WHERE log.Status='200 OK' AND name IS NOT NULL
    GROUP BY name
    ORDER BY views DESC;
''')

topAuthors = cur.fetchall()

# Query for days where more than 1% of request resulted in an error
cur.execute('''
    SELECT CAST(time AS DATE), (CAST(SUM(CAST(log.status!='200 OK' AS INT)) * 100 AS FLOAT(1)) / SUM(CAST(log.status IS NOT NULL AS INT))) AS Percentage
    FROM log
    GROUP BY CAST(time AS DATE)
    HAVING SUM(CAST(log.status!='200 OK' AS INT))*100/SUM(CAST(log.status IS NOT NULL AS INT))>1
    ORDER BY Percentage DESC;
''')

badDays = cur.fetchall()

# Outputs File with results
f = open("analysis.txt","w+")
f.write(str(topArticles) + str(topAuthors) + str(badDays))
f.close()
