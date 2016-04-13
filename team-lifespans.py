import csv
import TBAT

current_year = 2016

# I still need to fix my code to not need this
stop_page = 13

# set up data list
headers = [['team', 'founded', 'last active', 'years active', 'max possible years','ratio']]

with open('teaminfo.csv', 'w', newline='\n') as f:
    writer = csv.writer(f, delimiter=',')
    # for row in data:
    writer.writerow(headers)
f.close

# get list of teams, store in all_teams
all_teams = TBAT.get_all_teams(stop_page)
print(all_teams)

# TODO: get info associated with each team

# Add each team and its associated info to the data list
with open('teaminfo.csv', 'a', newline='\n') as f:
    writer = csv.writer(f, delimiter=',')
    for team in all_teams:
        years = TBAT.get_active_years(team)
        # TODO: Get rookie year from Team Info instead, use that in calculations
        try:
            rookie_year = TBAT.get_rookie_year(team)
        except TypeError:
            try:
                rookie_year = years[0]
            except IndexError:
                rookie_year = 'unknown'
        try:
            last_active = years[len(years)-1]
        except IndexError:
            last_active = 'n/a'
        years_active = len(years)
        try:
            max_years = current_year + 1 - rookie_year
        except TypeError:
            max_years = 'unknown'
        try:
            temp = [team, rookie_year, last_active, years_active, max_years, years_active/max_years]
        except TypeError:
            temp = [team, rookie_year, last_active, years_active, max_years, 0]
        print(temp)
        writer.writerow(temp)
    # data.append(temp)
f.close

# print(data)

# with open('teaminfo.csv', 'w', newline='\n') as f:
#     writer = csv.writer(f, delimiter=',')
#     for row in data:
#         writer.writerow(row)
