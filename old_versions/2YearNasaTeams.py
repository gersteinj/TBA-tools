import TBAT
import csv
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of Program\n')

# file = open('2yrNASA.csv', 'w', newline='',encoding='utf-8')
file = open('2yrteams.csv')
reader = csv.reader(file)

data = list(reader)

# close file
file.close()

headers = ['Team', 'Rookie Year', 'Full Name', 'NASA?']

# open second CSV file to write to
newFile = open('2yrNASA.csv', 'w', newline='')
writer = csv.writer(newFile, delimiter=',')
writer.writerow(headers)

# TODO: Load each row
for row in data[1:]:
    logging.debug('Checking team %s' % row[0])
    teamInfo = TBAT.get_team_info(row[0])
    teamName = str(teamInfo['name'])
    if 'NASA' in teamName.upper():
        nasaTeam = True
    else:
        nasaTeam = False
    newRow = [row[0], row[1], teamName, nasaTeam]
    writer.writerow(newRow)

newFile.close()
