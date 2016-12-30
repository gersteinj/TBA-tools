import pandas as pd
import pickle
data = {
        'Team': [11, 25, 225, 303, 747, 1257, 1626, 1676, 2590, 5624],
        'Name': ['MORT', 'Raider Robotix', 'Tech Fire', 'TEST Team', 'Flight Crew', 'Parallel Universe', 'Falcon Robotics', 'Pascack Pi-oneers', 'Nemesis', 'Tiger Tech'],
        'Location': ['Mount Olive', 'North Brunswick', 'York', 'Bridgewater', 'Middlesex', 'Scotch Plains', 'Metuchen', 'Pascack Valley', 'Robbinsville', 'South Plainfield']
        }

table = pd.DataFrame(data, index=data['Team'])

print(table)

# table.to_pickle('new_cache/sample.p')
print(table[303])
