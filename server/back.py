import sqlite3

# Function to create a database
def create_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
    ''')

    conn.commit()
    conn.close()
    print(f"Database '{db_name}' created successfully.")

# Function to search in the database
def search_in_database(db_name, name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE name=?", (name,))
    result = cursor.fetchall()

    conn.close()
    return result

# Function to add to the database
def add_to_database(db_name, name, age):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))

    conn.commit()
    conn.close()
    print(f"Record added to '{db_name}' successfully.")

# Function to delete from the database
def delete_from_database(db_name, user_id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))

    conn.commit()
    conn.close()
    print(f"Record with ID {user_id} deleted from '{db_name}'.")

# Function to update the database
def update_database(db_name, user_id, new_name, new_age):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET name=?, age=? WHERE id=?", (new_name, new_age, user_id))

    conn.commit()
    conn.close()
    print(f"Record with ID {user_id} updated in '{db_name}'.")

# Example usage:
# create_database('example.db')
# add_to_database('example.db', 'John Doe', 25)
# add_to_database('example.db', 'Jane Doe', 30)
# print(search_in_database('example.db', 'John Doe'))
# delete_from_database('example.db', 1)
# update_database('example.db', 2, 'Jane Doe Updated', 35)
