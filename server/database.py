import sqlite3
from faker import Faker

def create_word_database(database_name='word_dict.db'):
    # Connect to the database or create it if it doesn't exist
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    # Create the words table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL
        )
    ''')
    
    connection.commit()

    # Close the connection
    connection.close()

    


def insert_random_word(database_name='word_dict.db'):
    # Connect to the database
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    # Use faker to generate a random word
    fake = Faker()
    random_word = fake.word()

    # Insert the random word into the database
    cursor.execute('INSERT INTO words (word) VALUES (?)', (random_word,))

    connection.commit()

    # Close the connection
    connection.close()




def show_all_words(database_name='word_dict.db', pr = True):
    # Connect to the database
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    # Retrieve all words from the database
    cursor.execute('SELECT word FROM words')
    words = cursor.fetchall()

    # Close the connection
    connection.close()

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
    # create_word_database()

    # # Insert 10 random words into the database
    # for _ in range(10):
    #     insert_random_word()

    a, words = show_all_words()

    print(a)
    print(words)

    