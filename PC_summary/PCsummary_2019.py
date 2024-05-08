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
url = "https://en.wikipedia.org/wiki/2019_Indian_general_election_in_Delhi"

# Send HTTP request
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing election data
electiondata = soup.find("table", class_="wikitable")

election_tables = soup.find_all("table")
constituency = None

for table in election_tables:
    headers = table.find_all("th")
    for header in headers:
        if "Win Margin" in header.text:
            constituency=table
            break

for row in constituency.find_all("tr")[1:]:
    pc_no=row.find("th").text.strip()
    columns = row.find_all("td")
    constituency = columns[0].text.strip()
    turnout = columns[1].text.strip()
    elected_member = columns[2].text.strip()
    party=columns[4].text.strip()
    runner_up=columns[5].text.strip()
    runner_up_party=columns[7].text.strip()
    win_byvotes=columns[8].text.strip()
    win_bypercent=columns[9].text.strip()
    
    # Insert data into MySQL table 
    cur.execute("INSERT INTO PCResults_2019 (PC_No, Constituency, Turnout, Elected_Member, Party, Runner_up,Runner_up_Party, Win_Margin_by_votes, Win_Margin_by_percentage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                (pc_no, constituency, turnout, elected_member, party, runner_up, runner_up_party, win_byvotes, win_bypercent))

# Commit changes
con.commit()

print('Added to MySQL database')
# Close database connection