from django.db import models
from django.contrib import admin
from django.conf import settings

import pdb
import re

class UserProfile(models.Model):
    """
    Represent User entity
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    
    # email = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200, blank=True)    

    def __str__(self):
       return self.user.first_name + ' ' + self.user.last_name    

class Collection(models.Model):
    """
    Represent the n-n relationship between User & Game.
    Game_id fetch from Boardgamegeek API
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile)
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
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
    time = models.DateTimeField(auto_now=False, editable=True)
    main_game = models.CharField(max_length=200, blank=True)
    img_url = models.CharField(max_length=200, blank=True)    
    description = models.TextField()
    participants = models.ManyToManyField(UserProfile, through="Participant", blank=True)

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
    user = models.ForeignKey(UserProfile, related_name="players")
    event = models.ForeignKey(Event, related_name="players")
    is_host = models.BooleanField(default=False)

    def __str__(self):
        role = '';
        if self.is_host:
            role = " (Host)";
        return str(self.id) + " - " + self.event.name + " - " + str(self.user) + role

class Guild(models.Model):
    """
    Represent the Guild entity
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    hq = models.CharField(max_length=200)
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
    main_game = models.CharField(max_length=200, blank=True)
    img_url = models.CharField(max_length=200, blank=True)    
    description = models.TextField()
    member = models.ManyToManyField(UserProfile, related_name="members", through="GuildMember", blank=True)

    def __str__(self):
       return str(self.id) + ' - ' + self.name

class GuildMember(models.Model):
    """
    Represent the n-n relationship between Guild & User
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, related_name="memberships")
    guild = models.ForeignKey(Guild, related_name="memberships")
    is_leader = models.BooleanField(default=False)

    def __str__(self):
        role = '';
        if self.is_leader == True:
            role = " (Leader)";
        return str(self.id) + " - " + self.guild.name + " - " + str(self.user) + role