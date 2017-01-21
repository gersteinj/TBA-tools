import tbat
import pandas as pd
import pickle
import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG)

# data = {
#         'Team': [11, 25, 225, 303, 747, 1257, 1626, 1676, 2590, 5624],
#         'Name': ['MORT', 'Raider Robotix', 'Tech Fire', 'TEST Team', 'Flight Crew', 'Parallel Universe', 'Falcon Robotics', 'Pascack Pi-oneers', 'Nemesis', 'Tiger Tech'],
#         'Location': ['Mount Olive', 'North Brunswick', 'York', 'Bridgewater', 'Middlesex', 'Scotch Plains', 'Metuchen', 'Pascack Valley', 'Robbinsville', 'South Plainfield']
#         }

# table = pd.DataFrame(data, index=data['Team'])

# print(table)

# # table.to_pickle('new_cache/sample.p')
# print(table[303])


team_list = []

team_data = {
    'nickname': [],
    'city': [],
    'region': [],
    'country': [],
    'address': [],
    'rookie year': [],
    'years active': [],
    'lifespan': [],
    'motto': [],
    'website': [],
    'full name': []
}

teams = tbat.get_all_teams()

for team in teams:
    logging.info(team['team_number'])
    team_list.append(team['team_number'])
    team_data['nickname'].append(team['nickname'])
    team_data['city'].append(team['locality'])
    team_data['region'].append(team['region'])
    team_data['country'].append(team['country_name'])
    team_data['address'].append(team['location'])
    team_data['rookie year'].append(team['rookie_year'])
    try:
        years = tbat.get_team_years_participated(team['team_number'])
    except:
        years = []
    team_data['years active'].append(years)
    team_data['lifespan'].append(len(years))
    team_data['motto'].append(team['motto'])
    team_data['website'].append(team['website'])
    team_data['full name'].append(team['name'])    

df = pd.DataFrame(team_data, index=team_list)

print(df)

df.to_pickle('new_cache/full_team_dataframe.p')
