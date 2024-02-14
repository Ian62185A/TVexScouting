import requests
from bs4 import BeautifulSoup
url = "https://www.robotevents.com/robot-competitions/vex-robotics-competition/standings/skills?search=&event_region=Minnesota&country=244&region=34&grade_level=High+School"
response = requests.get(url)
response.find_all('td',class_='column-team-name')

