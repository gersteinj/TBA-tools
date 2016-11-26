import requests
import pprint
import logging

# logging configuration
logging.basicConfig(level=logging.DEBUG)

authorization = {'X-TBA-APP-ID':'jgerstein:TBAT:v2'}
base_url = 'https://www.thebluealliance.com/api/v2/'
team_url = base_url + 'team/frc'

def get_api_status():
	"""Checks status of the API"""
	r = requests.get(base_url + 'status', headers=authorization)
	logging.debug(r.json())
	return r.json()


def get_team_info(team_number):
	"""Gets info about a team"""
	r = requests.get(team_url + str(team_number), headers=authorization)
	data = r.json()
	logging.debug(data)
	return data


def get_team_list(page_num):
	"""Gets the specified page of the team list"""
	r = requests.get(base_url + 'teams/' + str(page_num), headers=authorization)
	data = r.json()
	logging.debug(data)
	return data


def get_all_teams():
	"""Returns a list of all teams"""
	# Create list to store teams in
	all_teams=[]
	page = 0
	# Will continue indefinitely
	while True:
		current_page = get_team_list(page)
		# Exit loop if team list contains no teams - we're at the end
		if len(current_page) == 0:
			break
		else:
			for team in current_page:
				all_teams.append(team)
		page += 1
	logging.debug(all_teams)
	return all_teams


def get_team_events(team_number, year=2016):
	"""Gets team events for a given year. Defaults to 2016"""
	r = requests.get(team_url + str(team_number) + '/' + str(year) + '/events', headers=authorization)
	data = r.json()
	logging.debug(data)
	return data


def get_team_event_awards(team_number, event):
	"""Gets a team's awards for a specified event"""
	r = requests.get(team_url + str(team_number) + '/event/' + event + '/awards', headers=authorization)
	data = r.json()
	logging.debug(data)
	return data


def get_team_event_matches(team_number, event):
	"""Gets a team's matches for a specified event"""
	r = requests.get(team_url + str(team_number) + '/event/' + event + '/matches', headers=authorization)
	data = r.json()
	logging.debug(data)
	return data


def get_team_years_participated(team_number):
	"""Gets a team's years participated in FRC"""
	r = requests.get(team_url + str(team_number) + '/years_participated', headers=authorization)
	data = r.json()
	logging.debug(data)
	return data


def get_team_media(team_number, year=2016):
	"""Returns a team's media for a specific year. Defaults to 2016"""
	r = requests.get(team_url + str(team_number) + '/' + str(year) + '/media', headers=authorization)
	data = r.json()
	logging.debug(data)
	return data


def get_team_event_history(team_number):
	"""Returns a team's event history"""
	r = requests.get(team_url + str(team_number) + '/history/events', headers=authorization)
	data = r.json()
	logging.debug(data)
	return data


# Test below this line
get_team_event_history(1257)