from django.db import models
from django.contrib import admin

import pdb
import re

class User(models.Model):
    """
    Represent User entity
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200, blank=True)

    def __str__(self):
       return str(self.id) + ' - ' + self.name

class Collection(models.Model):
    """
    Represent the n-n relationship between User & Game.
    Game_id fetch from Boardgamegeek API
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    game_id = models.CharField(max_length=200, blank=True)
    # make sure that user & game_id pair is unique in the database
    unique_together = ("user", "game_id")

class Event(models.Model):
    """
    Represent the game Event entity
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=False, editable=True)
    main_game = models.CharField(max_length=200)
    description = models.TextField()
    participants = models.ManyToManyField(User, through="Participant", blank=True)

    def get_games(self):
        # games = self.main_game[1:-1]
        # games = re.sub('\'', '', games)
        # return games
        return self.main_game

    def __str__(self):
       return str(self.id) + ' - ' + self.name

class Participant(models.Model):
    """
    Represent the n-n relationship between Event & User
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="players")
    event = models.ForeignKey(Event, related_name="players")
    is_host = models.BooleanField(default=False)

    def __str__(self):
        role = '';
        if self.is_host:
            role = " (Host)";
        return str(self.id) + " - " + self.event.name + " - " + self.user.name + role

class Guild(models.Model):
    """
    Represent the Guild entity
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    hq = models.CharField(max_length=200)
    description = models.TextField()
    member = models.ManyToManyField(User, related_name="members", through="GuildMember", blank=True)

    def __str__(self):
       return str(self.id) + ' - ' + self.name

class GuildMember(models.Model):
    """
    Represent the n-n relationship between Guild & User
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="memberships")
    guild = models.ForeignKey(Guild, related_name="memberships")
    is_leader = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)

    def __str__(self):
        role = '';
        if self.is_leader == True:
            role = " (Leader)";
        return str(self.id) + " - " + self.guild.name + " - " + self.user.name + role