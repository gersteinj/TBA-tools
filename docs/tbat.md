# TBAT

This is the starting point for TBA Tools. Once I've got everything set up, most people won't really need this part of the project. The functions simplify the process of retrieving data from the API, and part 2 uses those functions to accomplish higher level functionality.

<!-- MarkdownTOC -->

- General Purpose
    - Process Data
    - Get API Status
- Team Requests
    - Get Team Info
    - Get Team List
    - Get List of All Teams
    - Get Team Events
    - Get Team Event Awards
    - Get Team Event Matches
    - Get Team Years Participated
    - Get Team Media
    - Get Team Event History
    - Get Team Award History
- Event Requests
    - Get Events By Year
    - Get Event Info
    - Get Teams at Event
    - Get Event Matches
    - Get Event Statistics
    - Get Event District Points
    - Get Match
- District Requests
    - Get Districts
    - Get District Events
    - Get District Rankings
    - Get District Teams

<!-- /MarkdownTOC -->



## General Purpose

#### Process Data 

```python
process_data(api_response)
```

Processes data from an API request and returns a JSONified version.

#### Get API Status
```python
get_api_status()
```
Returns current status of the TBA API.

## Team Requests

#### Get Team Info
```python
get_team_info(team_number)

# example
get_team_info(1257)
```
Returns info about a team.

#### Get Team List
```python
get_team_list(page_num)

# example
get_team_list(2)
```
Returns the list of teams from a specific page. Each page contains teams starting at 500 * page_num and ending at start + 499.

#### Get List of All Teams
```python
get_team_list()
```
Returns a list of all teams, past and present.

#### Get Team Events
```python
get_team_events(team_number, [year])

# Examples
get_team_events(1257)
get_team_events(1257, 2014)
```
Returns the specified team's events for the specified year. If no year is provided, defaults to the current year.

#### Get Team Event Awards
```python
get_team_event_awards(team_number, event)

# Example
get_team_event_awards(1257, '2016njbri')
```
Returns the specified team's awards for the specified event. Event should be given as an event key using the official event codes.

#### Get Team Event Matches
```python
get_team_event_matches(team_number, event)

# Example
get_team_event_matches(1257, '2016njfla')
```
Returns the specified team's matches for the specified event. Event should be given as an event key using the official event codes.

#### Get Team Years Participated
```python
get_team_years_participated(team_number)

# example
get_team_years_participated(1257)
```
Returns a list of the years in which a team participated in FRC

#### Get Team Media
```python
get_team_media(team_number, [year])

# examples
get_team_media(1257, 2015)
get_team_media(1257)
```
Returns a list of team media for the specified year. Year defaults to current year if not specified.

#### Get Team Event History
```python
get_team_event_history(team_number)

# example
get_team_event_history(1257)
```
Returns a team's event history.

#### Get Team Award History
```python
get_team_awards_history(team_number)

# example
get_team_awards_history(1257)
```
Returns a list of the specified team's awards.

## Event Requests

#### Get Events By Year
```python
get_events_by_year([year])

# examples
get_events_by_year()
get_events_by_year(2014)
```
Returns a list of event keys for the specified year. Defaults to the current year if year is not specified.

#### Get Event Info
```python
get_event_info(event_key)

#examples
get_event_info('2016njbri')
get_event_info('2015njfla')
```
Returns information about the specified event. Event should be given as as an event key using the official event codes.

#### Get Teams at Event
```python
get_event_teams(event_key)

#example
get_event_info('2016njbri')
```
Returns a list of teams that attended the specified event. Event should be given as an event key using the official event codes.

#### Get Event Matches
```python
get_event_matches(event_key)

# example
get_event_matches('2016njfla')
```
Returns the specified event's matches. Event should be given as an event key using the official event codes.

#### Get Event Statistics
```python
get_event_stats(event_key)

# example
get_event_stats('2016njbri')
```
Returns the statistics for the specified event. Event should be given as an event key using the official event codes.

#### Get Event District Points
```python
get_event_district_points(event_key)

# example
get_event_district_points('2016njfla')
```
Returns the district points each team received at the specified event. Event should be given as an event key using the official event codes.

#### Get Match
```python
get_match(match_key)

<a name="example"></a>
# example
get_match('2016njfla_f1m1')
```
Returns info about a specific match.

## District Requests

#### Get Districts
```python
get_districts([year])

#examples
get_districts()
get_districts(2016)
```
Returns a list of districts for the specified year. If no year is specified, it defaults to the current year

#### Get District Events
```python
get_district_events(district_key, [year])

#examples
get_district_events(mar)
get_district_events(fim, 2014)
```
Returns a district's events for the specified year. If no year is specified, it defaults to the current year

#### Get District Rankings
```python
get_district_rankings(district_key, [year])

#examples
get_district_rankings(mar)
get_district_rankings(fim, 2014)
```
Returns a district's rankings for the specified year. If no year is specified, it defaults to the current year

#### Get District Teams
```python
get_district_teams(district_key, [year])

#examples
get_district_teams(mar)
get_district_teams(fim, 2014)
```
Returns a district's teams for the specified year. If no year is specified, it defaults to the current year
