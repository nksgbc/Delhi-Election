import requests
from bs4 import BeautifulSoup
import mysql.connector
import re

# Connect to MySQL database
con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='MySQL98',
    database='delhielection'
)
cur = con.cursor()

# URL of the Wikipedia page to scrape
url = "https://en.wikipedia.org/wiki/1999_Indian_general_election_in_Delhi"

# Send HTTP request
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing election data
electiondata = soup.find("table", class_="wikitable")

election_tables = soup.find_all("table", class_="wikitable")
constituency = None


for table in election_tables:
    headers = table.find_all("th")
    for header in headers:
        if "Party Affiliation" in header.text.strip():
            constituency=table
            break



for row in constituency.find_all("tr")[1:]:
    columns = row.find_all("td")
    no=columns[0].text.strip()
    constituency = columns[1].text.strip()
    elected_member = columns[2].text.strip()
    party=columns[3].text.strip()
    
    # Insert data into MySQL table 
    cur.execute("INSERT INTO PCResults_1999 (No, Constituency, Elected_Member, Party) VALUES (%s, %s, %s, %s)", 
                (no, constituency, elected_member, party))

# Commit changes
con.commit()

print('Added to MySQL database')
# Close database connection