#!python3
"""This script is meant to see if a league commissioner is trustworthy."""

#Imported packages
import requests

#Prompt user to enter their sleeper league ID
league_id = input('Enter your Sleeper League ID: ')
season = 2023

#Get all of the users in the league, this will tell us which user(s) is the commissioner
response = requests.get(f'https://api.sleeper.app/v1/league/{league_id}/users')
league_users = response.json()

#assign variables for the commissioner's user ID and display name, made them lists in case there is multiple commissioners
commissioner = []
display_name = []

#iterate through list of users in your league to find the commissioner(s) and assign their user ID and display name to variables
for i, stuff in enumerate(league_users):
    if league_users[i]['is_owner'] == True:
        commissioner.append(league_users[i]['user_id'])
        display_name.append(league_users[i]['display_name'])
        
#iterate through list of commissioners user IDs
for i, j in enumerate(commissioner):
    leagues_commissioned = 0
    normal_leagues = 0
    
    #get all of the leagues the commissioner is in
    response = requests.get(f'https://api.sleeper.app/v1/user/{commissioner[i]}/leagues/nfl/2023')
    commissioners_leagues = response.json()
    print(display_name[i], 'is in', len(commissioners_leagues), 'leagues. He is your commissioner.')
    
    #iterate through the list of leagues that the commissioner is in
    for k, l in enumerate(commissioners_leagues):
        #get the users in the league that we are looking at
        response = requests.get(f"https://api.sleeper.app/v1/league/{commissioners_leagues[k]['league_id']}/users")
        league_users = response.json()
        
        #iterate through the list of users in the leagues
        for o, p in enumerate(league_users):
            if league_users[o]['user_id'] == commissioner[i]:
                if league_users[o]['is_owner'] == True:
                    leagues_commissioned +=1
                else:
                    normal_leagues +=1
        
    print(display_name[i], 'is the commissioner of', leagues_commissioned, 'leagues. He is in', normal_leagues, 'leagues where he is not a commissioner.')
