import tbat
import logging
import pickle

logging.basicConfig(level=logging.INFO)


class Team(object):

    def __init__(self, results):
        """Return a Team object corresponding to the specified team"""
        self.website = results['website']
        self.nickname = results['nickname']
        self.locality = results['locality']
        self.region = results['region']
        self.country_name = results['country_name']
        self.location = results['location']
        self.team_number = results['team_number']
        self.name = results['name']
        self.rookie_year = results['rookie_year']
        self.motto = results['motto']
        self.key = results['key']
        self.years_active = tbat.get_team_years_participated(results['team_number'])
        events = []
        temp_events = tbat.get_team_event_history(results['team_number'])
        for event in temp_events:
            events.append(event['key'])
        self.event_history = events
        self.award_history = tbat.get_team_awards_history(results['team_number'])


class Event(object):

    def __init__(self, results):
        self.name = results['name']
        self.event_type = results['event_type']
        self.event_district = results['event_district']
        # self.facebook_eid = results['facebook_eid']
        self.event_code = results['event_code']
        self.week = results['week']
        self.start_date = results['start_date']
        self.location = results['location']
        self.type_string = results['event_type_string']
        self.alliances = results['alliances']
        self.end_date = results['end_date']
        self.key = results['key']
        self.short_name = results['short_name']
        self.website = results['website']
        self.webcast = results['webcast']
        self.venue_address = results['venue_address']
        self.year = results['year']
        self.district_string = results['event_district_string']
        self.official = results['official']
        self.timezone = results['timezone']


def update_individual_event(event_key):
    """Fetches event info about specified event."""
    # Get info about event
    e = tbat.get_event_info(event_key)
    # Create event object
    event = Event(e)
    filename = str(event_key) + '.p'
    with open('cached_data/' + filename, 'wb') as event_info:
        pickle.dump(event, event_info)
    return event


def load_individual_event(event_key):
    filename = str(event_key) + '.p'
    with open('cached_data/' + filename, 'rb') as event_info:
        event = pickle.load(event_info)
    return event

def update_team_info(test=''):
    """Fetches all team info. Do only as needed."""
    # Get all teams
    if(test == 'test'):
        all_teams = tbat.get_team_list(0)
    else:
        all_teams = tbat.get_all_teams()

    # Create objects
    teams = {}
    for team in all_teams:
        teams[team['team_number']] = Team(team)
        logging.info('%s complete' % team['team_number'])
    with open('cached_data/all_teams.p', 'wb') as all_teams:
        pickle.dump(teams, all_teams)
    return teams


def load_team_info():
    """Loads the save team info. Remember to import the Team class"""
    data = open('cached_data/all_teams.p', 'rb')
    teams = pickle.load(data)
    data.close()
    return teams


# Test below this line
if __name__ == "__main__":
    bri = load_individual_event('2016njbri')
    print(dir(bri))