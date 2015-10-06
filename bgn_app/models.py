from django.db import models

# Create your models here.

# Represent User entity
class User(models.Model):
  id          = models.AutoField(primary_key = True)
  name        = models.CharField(max_length = 200)
  email       = models.CharField(max_length = 200)
  location    = models.CharField(max_length = 200)
  img_url     = models.CharField(max_length = 200)

# Represent Game entity
class Game(models.Model):
  id          = models.AutoField(primary_key = True)
  name        = models.CharField(max_length = 200)
  player_min  = models.IntegerField()
  player_max  = models.IntegerField()

# Represent the n-n relationship between User & Game
class Collection(models.Model):
  id          = models.AutoField(primary_key = True)
  user        = models.ForeignKey(User)
  game        = models.ForeignKey(Game)

# Represent Tags for Games
class Tag(models.Model):
  id          = models.AutoField(primary_key = True)
  name        = models.CharField(max_length = 200)

# Represent the n-n relationship between Game & Tags
class GameTags(models.Model):
  id          = models.AutoField(primary_key = True)
  game        = models.ForeignKey(Game)
  tag         = models.ForeignKey(Tag)

# Represent the game Event entity
class Event(models.Model):
  id          = models.AutoField(primary_key = True)
  venue       = models.CharField(max_length = 200)
  time        = models.DateTimeField()
  host        = models.ForeignKey(User)
  main_game   = models.ForeignKey(Game)
  description = models.TextField()

# Represent the n-n relationship between Event & User
class Participants(models.Model):
  id          = models.AutoField(primary_key = True)
  event       = models.ForeignKey(Event)
  user        = models.ForeignKey(User)
