import pandas as pd
import sqlite3



def create_table(cursor):
    # Define the CREATE TABLE SQL query
    create_table_query = """
    CREATE TABLE IF NOT EXISTS products (
        Name TEXT,
        Brand TEXT,
        Price INTEGER,
        DiscountedPrice INTEGER,
        Category TEXT,
        SubCategory TEXT,
        Quantity TEXT,
        Description TEXT
    );
    """
    # Execute the query
    cursor.execute(create_table_query)


def insert_data(cursor, csv_file):
    # Read data from CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Insert data into the 'products' table
    df.to_sql('products', conn, if_exists='replace', index=False)


def get_table_shape(cursor):
    # Get the shape of the table
    cursor.execute("SELECT COUNT(*) FROM products;")
    rows_count = cursor.fetchone()[0]

    cursor.execute("PRAGMA table_info(products);")
    columns_count = len(cursor.fetchall())

    return rows_count, columns_count


def show_description(cursor):
    cursor.execute("PRAGMA table_info(products);")
    columns_info = cursor.fetchall()
    column_descriptions = [(col[1], col[2]) for col in columns_info]
    for col_name, col_type in column_descriptions:
        print(f"{col_name}: {col_type}")


def show_elements(cursor, num_elements, pr=True):
    query = f"SELECT * FROM products LIMIT {num_elements};"
    cursor.execute(query)
    rows = cursor.fetchall()
    
    if rows:
        columns = [description[0] for description in cursor.description]
        df = pd.DataFrame(rows, columns=columns)
        if pr:
            print(df)
        json_data = df.to_json(orient='records')
        return json_data
    else:
        print("No elements found in the table.")
        return None



if __name__ == '__main__':
    from database import returnCursor, closeConn
    # Connect to the SQLite database
    conn , cursor = returnCursor()

    # Create the 'products' table
    #create_table(cursor)

    # Insert data from CSV file into the 'products' table
    #csv_file_path = 'DMart.csv'  # Replace with the actual path to your CSV file
    #insert_data(cursor, csv_file_path)

    # Get the shape of the 'products' table
    table_shape = get_table_shape(cursor)
    print(f"Table Shape: {table_shape}")

    # Show the description of the 'products' table
    show_description(cursor)

    # Show the first 5 elements of the 'products' table
    show_elements(cursor, 5)

    # Commit changes and close the connection
    closeConn(conn)
