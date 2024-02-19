import sqlite3
from faker import Faker

def create_word_database(cursor):
    # Create the words table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL
        )
    ''')


    


def insert_random_word(cursor):
    # Use faker to generate a random word
    fake = Faker()
    random_word = fake.word()

    # Insert the random word into the database
    cursor.execute('INSERT INTO words (word) VALUES (?)', (random_word,))




def show_all_words(cursor, pr = True):
    # Retrieve all words from the database
    cursor.execute('SELECT word FROM words')
    words = cursor.fetchall()

    # Display the words
    if words:
        if pr:
            print("All words in the database:")
            for word in words:
                print(word[0])
        
        # Return the length of the list of words
        return len(words) , words
    else:
        if pr:
            print("No words found in the database.")
        return 0, []



    
if __name__ == '__main__':
    from database import returnCursor, closeConn

    # Connect to the SQLite database
    conn , cursor = returnCursor()
    #create_word_database(cursor)

    # Insert 10 random words into the database
    #for _ in range(980):
    #    insert_random_word(cursor)

    a, words = show_all_words(cursor)

    print(a)
    #print(words)
    closeConn(conn)

    