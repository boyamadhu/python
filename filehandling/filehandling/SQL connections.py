def conne():
    import sqlite3
    connobj=sqlite3.connect('madhu.db')
    return connobj
connobj=conne()

def create_table(connobj):
    cursobj=connobj.cursor()
    cursobj.execute('create table emp(id integer primary key,name text unique)')
    print('table created')
#create_table(connobj)


def insert_data(connobj):
    cursobj=connobj.cursor()
    cursobj.execute('insert into emp values(1,"madhu")')
    print(connobj)
insert_data(connobj)

def insert_data(connobj):
    cursobj=connobj.cursor()
    
    cursobj.execute('drop table emp')
    print('table droped successfully')
#insert_data(connobj)

def retrieve_data(connobj):
    cursor=connobj.cursor()
    x=cursor.execute('select * from emp')
    for i in x:
        print(i)
retrieve_data(connobj)
    
