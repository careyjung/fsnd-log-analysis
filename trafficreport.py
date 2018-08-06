#!/usr/bin/env python3

#
# Full Stack Web Developer Log Analysis Project
# Carey Jung, carey.jung@gmail.com
#

import psycopg2
import datetime

# What are the most popular three articles of all time?
query1 = """
    select articles.title, count(articles.slug) as hits
    from articles left join log on '/article/' || articles.slug = log.path
    group by articles.title, log.path
    order by hits desc limit 3
"""

# Who are the most popular article authors of all time?
query2 = """
select authors.name, hits from authors left join
    (select articles.author, count(articles.author) as hits
        from articles left join log on '/article/' || articles.slug = log.path
        group by articles.author
        order by hits desc) authorhits on authors.id = authorhits.author
"""
# On which days did more than 1% of requests lead to errors?
# (See README.md for errorsbydate and trafficbydate views.)
query3 = """
select errorsbydate.date as date,
        errors,
        views,
        errors::float/views*100.0 as pct
    from errorsbydate join trafficbydate on
        errorsbydate.date = trafficbydate.date and
        errorsbydate.errors > .01*trafficbydate.views;
"""

db = psycopg2.connect("dbname=news")
cursor = db.cursor()

today = datetime.date.today()

print('{:>40s}'.format('News Traffic Report'))
print('{:>30d}-{:02d}-{:02d}\n'.format(today.year, today.month, today.day))


cursor.execute(query1)
print("The most popular three articles of all time are:")
for article in cursor.fetchall():
    print('{:>40} -> {:>8,d} views'.format(article[0], article[1]))
print('')

cursor.execute(query2)
print('The most popular authors of all time are:')
for author in cursor.fetchall():
    print('{:>40} -> {:>8,d} views'.format(author[0], author[1]))
print('')

cursor.execute(query3)
print('The days with more than 1% of requests leading to errors are:')
for errors in cursor.fetchall():
    print('{:>40} -> {:7.2f}% errors'.format(str(errors[0]), errors[3]))
print('')

db.close()
