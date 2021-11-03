
def closeMysqlconnection(mysql_db, my_cursor):
    if mysql_db.is_connected():
            mysql_db.close()            
            my_cursor.close()
            print("MySQL connection is closed")
