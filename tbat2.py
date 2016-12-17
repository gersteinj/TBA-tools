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
    # teams = fetch_team_info()
    # for team in teams:
    #     print("Team %s is from %s. They are typically called %s. They were active in %s" % (team.team_number, team.locality, team.nickname, team.years_active))
    all_teams = load_team_info()
    print(all_teams)
