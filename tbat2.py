import tbat


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


def fetch_team_info():
    """Fetches all team info. Do only as needed."""
    # Get all teams
    all_teams = tbat.get_all_teams()

    # Create objects
    teams = []
    for team in all_teams:
        teams.append(Team(team))
    return teams


# Test below this line
teams = fetch_team_info()
for team in teams:
    print("Team %s is from %s. They are typically called %s. They were active in %s" % (team.team_number, team.locality, team.nickname, team.years_active))