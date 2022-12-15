#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 12:26:15 2022

@author: karlsteen
"""
#   Skapa 4 olika klasser med 3 olika attribut och 3 olika metoder. Samt getters och setters. 
#   Notera att ni måste lägga lite tid på modeleringen av klasserna, så att de är logiska och har en mening

class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        
    def add_player(self, player):
        self.players.append(player)
        
    def remove_player(self, player):
        self.players.remove(player)
        
    def display_players(self):
        for player in self.players:
            print(player)
            
class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
class Game:
    def __init__(self, home_team, away_team, date):
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        
    def display_game_info(self):
        print("The {} will play against the {} on {}.".format(self.home_team.name, self.away_team.name, self.date))
        
class League:
    def __init__(self, name, teams):
        self.name = name
        self.teams = teams
        
    def add_team(self, team):
        self.teams.append(team)
        
    def remove_team(self, team):
        self.teams.remove(team)
        
    def display_teams(self):
        for team in self.teams:
            print(team.name)