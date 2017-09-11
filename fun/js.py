# -*- encoding=utf-8 -*-
import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='',
        db ='',
        charset='utf8'
        )
cur = conn.cursor()
def end():
    cur.close()
    conn.commit()
    conn.close()

#借书
def j_book(id):
    cur.execute("update book set bk_status=1 where id="+id)
    end()

#查在库书籍
def k_book():
    num0=cur.execute("select * from book where bk_status=0")
    info = cur.fetchmany(num0)
    end()
    return info
#查外借书籍
def n_book():
    num1=cur.execute("select * from book where bk_status=1")
    info = cur.fetchmany(num1)
    end()
    return info



