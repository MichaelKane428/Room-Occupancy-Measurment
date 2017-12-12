
import MySQLdb


def login_connection():
    conn = MySQLdb.connect(host="localhost",
                           user="root",
                           passwd="Mikey1ne",
                           db="fyp")
    dbcursor = conn.cursor()

    return dbcursor, conn
