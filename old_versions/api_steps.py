import requests

URL = 'http://www.thebluealliance.com/api/v2/'
header = {'X-TBA-App-Id': 'jgerstein:api-lesson:v02'}

myRequest = (URL + 'team/frc1257')
response = requests.get(myRequest, headers=header)

jsonified = response.json()

print(jsonified)

for key in jsonified.keys():
    print(key)
# print(jsonified['website'])

print(jsonified['nickname'])
