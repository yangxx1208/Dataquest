## 3. Psycopg2 ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
print(cur)
conn.close()

## 4. Creating a table ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
query = '''create table notes (
id integer,
body text,
title text);'''
cur.execute(query)
conn.close()

## 5. SQL Transactions ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
query = '''create table notes 
(id integer primary key,
body text,
title text)'''
cur.execute(query)
conn.commit()
conn.close()




## 6. Autocommitting ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
conn.autocommit = True
cur.execute('''create table facts (id integer primary key,
           country text,
           value integer)''')
conn.close()

## 7. Executing queries ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("insert into notes values(1,'Do more missions on Dataquest','Dataquest reminder')")
cur.execute("select * from notes")
notes = cur.fetchall()
print(notes)
conn.close()


## 8. Creating a database ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
conn.autocommit = True
cur.execute("CREATE DATABASE income OWNER dq;")
conn.close()

## 9. Deleting a database ##

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute("DROP DATABASE income;")
conn.close()