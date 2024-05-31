import sqlite3

# Full path to the SQLite database file
database_path = r'D:\Python_CA\Duombaze\sample.db'

# Connect to the SQLite database
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Create a table with an auto-incrementing primary key
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

# Commit the changes
conn.commit()

# Function to insert a user into the users table using parameters
def insert_user(name):
    cursor.execute('''
        INSERT INTO users (name) VALUES (:name)
    ''', {'name': name})
    conn.commit()

# Ask the user for input and insert the provided name
user_name = input("Enter your name: ")
insert_user(user_name)
print("User inserted successfully.")

# Fetch and display the data to verify
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()


print("Github")