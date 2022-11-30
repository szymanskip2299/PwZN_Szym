
#poetry run python .\proj4.py hacker.json

import requests
from bs4 import BeautifulSoup
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_name",type = str)
args = parser.parse_args()
file_name=args.file_name


req = requests.get('https://wiki.hackerspaces.org/Projects')
soup = BeautifulSoup(req.text, 'html.parser')

hacker_projects = soup.find('table', {'class': "sortable wikitable smwtable broadtable"})


projects=[]

for entry in hacker_projects.find('tbody').find_all('tr')[1:]:#pierwsze to metadane
    project=entry.find("td",{'class': "smwtype_wpg"})
    keywords=entry.find("td",{'class': "Keywords smwtype_txt"})
    date=entry.find("td",{'class': "Modification-date smwtype_dat"})
    print(f"{project.text.strip()} | {keywords.text.strip()} | {date.text.strip()}")
    projects.append((project.text.strip(),keywords.text.strip(),date.text.strip()))

with open(file_name, 'w') as f:
    json.dump(projects, f)