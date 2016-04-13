import csv
import TBAT

current_year = 2016

# I still need to fix my code to not need this
stop_page = 13

# set up data list
data = [['team', 'founded', 'last active', 'years active', 'max possible years','ratio']]

# get list of teams, store in all_teams
all_teams = TBAT.get_all_teams(stop_page)
print(all_teams)

# TODO: get info associated with each team

# Add each team and its associated info to the data list
for team in all_teams:
    years = TBAT.get_active_years(team)
    rookie_year = years[0]
    last_active = years[len(years)-1]
    years_active = len(years)
    max_years = current_year + 1 - rookie_year
    temp = [team, rookie_year, last_active, years_active, max_years, years_active/max_years]
    print(temp)
    data.append(temp)

print(data)

with open('teaminfo.csv', 'w', newline='\n') as f:
    writer = csv.writer(f, delimiter=',')
    for row in data:
        writer.writerow(row)
