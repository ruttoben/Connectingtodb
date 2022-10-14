import psycopg2


def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='one2eight' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='one2eight' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='one2eight' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute('SELECT * FROM store')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='one2eight' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute('DELETE FROM store WHERE item=%s ', (item, ))
    conn.commit()
    conn.close()


def update(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='one2eight' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute('UPDATE store SET price=?, quantity=? WHERE item=?', (item, quantity, price))
    conn.commit()
    conn.close()


create_table()
insert('apples', 10, 15)
# delete('orange')
print(view())
