import requests
# import pprint
# pp = pprint.PrettyPrinter()

URL = 'http://www.thebluealliance.com/api/v2/'

HEADER_KEY = 'X-TBA-App-Id'
HEADER_VAL = 'jgerstein:APItest:v01'
header = {HEADER_KEY: HEADER_VAL}

# TODO: figure out how to make the function identify the last page
def get_all_teams(last_page):
    all_teams = []

    # For each page through the last one, request list of teams
    for pg in range(last_page):
        r = (URL + 'teams/' + str(pg))
        response = requests.get(r, headers=header)

        jsonified = response.json()
        for team in jsonified:
            all_teams.append(team['team_number'])

    return all_teams


def get_active_years(team_num):
    years = []

    r = (URL + 'team/' + 'frc' + str(team_num) + '/years_participated')
    response = requests.get(r, headers=header)

    jsonified = response.json()
    for year in jsonified:
        years.append(year)

    years.sort()

    return years


def active_in_year(team_num, year):
    years = get_active_years(team_num)

    if year in years:
        return True
    else:
        return False

'''
# Get list of all teams
# historic_team_list = get_all_teams(14)
historic_team_list = get_all_teams(1)
print(historic_team_list)
# Check if each team is active in specified year
for team in historic_team_list:
    if active_in_year(team, 2016):
        print(str(team) + ' is active')
    else:
        print(str(team) + ' is no longer active')
# TODO: If team is active, add them to a new list

print(active_in_year(1257, 2016))
'''