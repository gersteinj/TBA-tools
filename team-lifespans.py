import csv
import TBAT

current_year = 2016

# set up data list
data = [['team', 'founded', 'last competed' 'years active', 'max possible years']]

# get list of teams, store in all_teams
all_teams = TBAT.get_all_teams(1)
print(all_teams)

# TODO: get info associated with each team

# Add each team and its associated info to the data list
for team in all_teams[:5]:
    years = TBAT.get_active_years(team)
    temp = [team, years[0], years[len(years)-1], len(years), current_year + 1 - years[0]]
    data.append(temp)

print(data)

with open('teaminfo.csv', 'w', newline='\n') as f:
    writer = csv.writer(f, delimiter=',')
    for row in data:
        writer.writerow(row)
