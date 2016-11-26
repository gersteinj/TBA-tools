import requests
# import json
import pprint
pp = pprint.PrettyPrinter()

URL = 'http://www.thebluealliance.com/api/v2/'

HEADER_KEY = 'X-TBA-App-Id'
HEADER_VAL = 'jgerstein:APItest:v01'
header = {HEADER_KEY: HEADER_VAL}


def get_team_info(team_key):
        myRequest = str(URL + 'team/' + team_key)
        response = requests.get(myRequest, headers=header)

        return response.json()


def get_event_info(event_key):
        myRequest = str(URL + 'event/' + event_key)
        response = requests.get(myRequest, headers=header)

        return response.json()


def teams_at_event(event_key):
        myRequest = str(URL + 'event/' + event_key + '/teams')
        response = requests.get(myRequest, headers=header)

        jsonified = response.json()

        teams = []

        for team in jsonified:
                teams.append(team['team_number'])

        teams.sort()

        return teams

print(get_event_info('2016njfla'))

# request = urllib.request.Request(URL + 'event/' + event_key + '/teams')
# request.add_header(HEADER_KEY, HEADER_VAL)
# response = urllib.request.urlopen(request)
# jsonified = json.loads(response.read().decode("utf-8"))
# teams = []

# for team in jsonified:
#         teams.append(team['key'])

# print(teams)