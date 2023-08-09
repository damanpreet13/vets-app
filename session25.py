# Web Scrapping :)
# pip install beautifulsoup4
# pip install requests
import requests
from bs4 import BeautifulSoup

url = "https://www.espncricinfo.com/series/indian-premier-league-2023-1345038/points-table-standings"

response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')

teams = soup.find_all('span', class_="ds-text-tight-s ds-font-bold ds-uppercase ds-text-left ds-text-typo")
wins = soup.find_all('td', class_="ds-w-0 ds-whitespace-nowrap ds-min-w-max")
# List of Dictionaries
data = []

for idx in range(10):
    team_data = []
    data.append(team_data)

print("data:", data)

idx = 0
for team in teams:
    title = team.text.strip()
    data[idx].append(title)
    idx += 1
print("data:", data)


team_idx = 0
idx = 0

for win in wins:
    num = win.text.strip()
    print(num)
    data[team_idx].append(num)
    idx += 1

    if idx % 8 == 0:
        print("Wow....")
        team_idx += 1

print("data finally:", data)


file = open("ipl-data-2023.csv", "a")
header = "TEAMS,M,W,l,T,N/R,NRR,For,Against\n"
file.write(header)
for info in data:
    csv = "{},{},{},{},{},{},{},{},{}\n"\
        .format(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8])

    file.write(csv)

    print(csv)

print("Check the File...")