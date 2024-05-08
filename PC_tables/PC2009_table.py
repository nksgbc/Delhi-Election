import mysql.connector

try:
    # Connect to MySQL database
    con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='MySQL98',
    database='delhielection'
)

    if con.is_connected():
        print('Connected to MySQL database')

except mysql.connector.Error as error:
    print(f'Error connecting to MySQL database: {error}')

con.cursor().execute("""
    CREATE TABLE IF NOT EXISTS PCResults_2009 (
        PC_No INT PRIMARY KEY,
        Constituency TEXT,
        Turnout TEXT,
        Elected_Member TEXT,
        Party TEXT,
        Win_Margin_by_votes TEXT
    )""");


# Commit the transaction
con.commit()

print("Table created")