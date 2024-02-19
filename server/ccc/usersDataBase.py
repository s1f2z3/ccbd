import sqlite3
from faker import Faker
import hashlib
from prettytable import PrettyTable

# Function to create the 'user' table
def create_user_table(cursor):
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                user_name TEXT,
                email TEXT,
                pass TEXT,
                hashpass TEXT,
                UNIQUE(id)
            )
        ''')
        print("Table 'user' created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating 'user' table: {e}")

# Function to insert a fake user into the 'user' table
def insert_fake_user(cursor):
    fake = Faker()
    user_name = fake.user_name()
    email = fake.email()
    password = fake.password()

    # Hashing the password using hashlib
    hashpass = hashlib.sha256(password.encode()).hexdigest()

    try:
        cursor.execute('''
            INSERT INTO users (user_name, email, pass, hashpass)
            VALUES (?, ?, ?, ?)
        ''', (user_name, email, password, hashpass))
        #print("Fake user inserted successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting fake user: {e}")

# Function to display all users in the 'user' table
def display_users(cursor):
    try:
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()

        if users:
            table = PrettyTable(["ID", "User Name", "Email", "Password", "Hashed Password"])
            for user in users:
                table.add_row(user)

            print(table)
            print(f"Total users: {len(users)}")
        else:
            print("No users found.")
    except sqlite3.Error as e:
        print(f"Error displaying users: {e}")


def check_user_credentials(cursor, user_name, hashpass):
    try:
        cursor.execute('''
            SELECT id FROM users
            WHERE user_name = ? AND hashpass = ?
        ''', (user_name, hashpass))

        user_id = cursor.fetchone()

        if user_id:
            return user_id[0]  # Return the user_id if credentials are correct
        else:
            return 0  # User not found or credentials are incorrect

    except sqlite3.Error as e:
        print(f"Error checking user credentials: {e}")
        return -1  # Error occurred while checking credentials



def drop_user_table(cursor):
    try:
        cursor.execute('''DROP TABLE IF EXISTS users''')
        print("Table 'users' dropped successfully.")
    except sqlite3.Error as e:
        print(f"Error dropping 'user' table: {e}")


# Example usage
if __name__ == "__main__":
    from tqdm import tqdm
    from database import returnCursor, closeConn

    # Get a cursor to the database
    conn, cursor = returnCursor()
    #drop_user_table(cursor)

    # Create 'user' table
    # create_user_table(cursor)

    # Insert a fake user
    # for i in tqdm(range(1000)):
    #     insert_fake_user(cursor)

    # Display all users
    display_users(cursor)

    # Commit changes and close the connection
    closeConn(conn)
