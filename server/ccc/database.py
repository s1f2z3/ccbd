import sqlite3

def returnCursor():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    return conn, cursor


def closeConn(conn):
    conn.commit()
    conn.close()


def show_tables(cursor):
    # Execute a query to get the list of tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # Fetch all the table names
    tables = cursor.fetchall()

    # Print the table names
    print("Tables in the database:")
    for table in tables:
        print(table[0])



if __name__ == '__main__':
    conn, cursor= returnCursor()
    show_tables(cursor)
    closeConn(conn)