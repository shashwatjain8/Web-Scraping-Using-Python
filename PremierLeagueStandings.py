# Scraping PL Standings from ESPN League Page

import requests
from bs4 import BeautifulSoup
import pandas as pd

def getScoreTable():
    url = "http://www.espn.in/football/table/_/league/eng.1"
    contest_file = requests.get(url)
    soup = BeautifulSoup(contest_file.text, 'html.parser')

    row = soup.find_all("tr", attrs={'class': 'standings-row'})

    table = []

    for i in row:
        team = []
        for j in i:
            team.append(j.text)
            if len(team) == 9:
                table.append(team)

    team_name = []
    games_played = []
    wins = []
    draws = []
    losses =[]
    goals_for = []
    goals_against = []
    goals_difference = []
    points = []

    for i in range(0, 20):
        x = str(i+1)
        team_name.append(table[i][0].strip(x))
        games_played.append(table[i][1])
        wins.append(table[i][2])
        draws.append(table[i][3])
        losses.append(table[i][4])
        goals_for.append(table[i][5])
        goals_against.append(table[i][6])
        goals_difference.append(table[i][7])
        points.append(table[i][8])

    df = pd.DataFrame(columns={"Position", "Team", "Games", "Wins", "Draws", "Losses", "For", "Against", "Goals Difference", "Points"})

    pos = []
    for i in range(1,21):
        pos.append(i)

    df["Position"] = pos
    df["Team"] = team_name
    df["Games"] = games_played
    df["Wins"] = wins
    df["Draws"] = draws
    df["Losses"] = losses
    df["For"] = goals_for
    df["Against"] = goals_against
    df["Goals Difference"] = goals_difference
    df["Points"] = points
    number = input('Enter Number of top teams to see')
    print df[:number]


getScoreTable()