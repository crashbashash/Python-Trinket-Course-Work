#!/bin/python3

from random import choice ##Import choice from random to select a random item in a list
import os ##Import os to get the run location of the script we are running

runLoc = os.path.dirname(os.path.realpath(__file__))+"/" ##Store the location of the python script we are currently running

players = open(runLoc+"Players.txt", "r").read().splitlines() ##List of available players pulled from a txt file
teams =  open(runLoc+"TeamNames.txt", "r").read().splitlines() ##List of available team names pulled from a txt file

teamA = [] ##Instantiate Team A's player list
teamB = [] ##Instantiate Team B's player list
teamC = [] ##Instantiate Team C's player list

##Choose Team A's name
teamAName = choice(teams)
teams.remove(teamAName)

##Choose Team B's name
teamBName = choice(teams)
teams.remove(teamBName)

##Choose Team C's name
teamCName = choice(teams)
teams.remove(teamCName)

while len(players) > 0: ##Loop to add players to both teams
    try:
        p = choice(players)
        teamA.append(p) ##Append the chosen player to Team A's list
        players.remove(p) ##Remove that player from the list of available players

        p = choice(players)
        teamB.append(p) ##Append the chosen player to Team B's list
        players.remove(p) ##Remove that player from the list of available players

        p = choice(players)
        teamC.append(p) ##Append the chosen player to Team C's list
        players.remove(p) ##Remove that player from the list of available players
    except IndexError:
        break


print(F"{teamAName}: {teamA}\n{teamBName}: {teamB}\n{teamCName}: {teamC}") ##Print the players in each team
