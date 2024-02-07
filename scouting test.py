import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = "https://www.robotevents.com/robot-competitions/vex-robotics-competition/standings/skills?search=&event_region=Minnesota&country=244&region=34&grade_level=High+School"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element that contains the data you want to extract
    # For example, let's say you want to extract all team names
    team_names = soup.find_all('span', class_='team-name')
   
    # Extract and print the team names
    for name in team_names:
        print(name.text)
else:
    print("Failed to retrieve data from the website.")



