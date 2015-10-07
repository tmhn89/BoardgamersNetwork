from django.db import models

# Create your models here.

# Represent User entity
class User(models.Model):
  id          = models.AutoField(primary_key = True)
  name        = models.CharField(max_length = 200)
  email       = models.CharField(max_length = 200)
  location    = models.CharField(max_length = 200)
  img_url     = models.CharField(max_length = 200)
  friendships = models.ManyToManyField('self', through='FriendShips',
                                        symmetrical=False,
                                        related_name='related_to+')

  def add_friendship(self, user, symm=True):
    friendships, created = FriendShips.objects.get_or_create(
        from_person=self,
        to_person=user)
    if symm:
        # avoid recursion by passing `symm=False`
        user.add_friendship(self, False)
    return friendships

  def remove_friendship(self, user, symm=True):
    FriendShips.objects.filter(
        from_person=self,
        to_person=user).delete()
    if symm:
        # avoid recursion by passing `symm=False`
        user.remove_friendship(self, False)

  def get_friends(self):
    return self.friendships.filter(
        to_people__from_person=self,
        from_people__to_person=self)


# Represent the n-n relationship between User & Game. Game_id fetch from Boardgamegeek API
class Collection(models.Model):
  id          = models.AutoField(primary_key = True)
  user        = models.ForeignKey(User)
  game_id     = models.CharField(max_length = 200, blank = True)
  # make sure that user & game_id pair is unique in the database
  unique_together = ("user", "game_id")

# Represent the game Event entity
class Event(models.Model):
  id          = models.AutoField(primary_key = True)
  venue       = models.CharField(max_length = 200)
  time        = models.DateTimeField()
  host        = models.ForeignKey(User)
  main_game   = models.CharField(max_length = 200)
  description = models.TextField()

# Represent the n-n relationship between Event & User
class Participants(models.Model):
  id          = models.AutoField(primary_key = True)
  event       = models.ForeignKey(Event)
  user        = models.ForeignKey(User)

# Represent the friendship between two Users
class FriendShips(models.Model):
  # if user's have added each others as friends, a FriedShips will be created
  from_person = models.ForeignKey(User, related_name='from_people')
  to_person = models.ForeignKey(User, related_name='to_people')

