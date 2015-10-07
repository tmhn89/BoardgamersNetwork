from django.shortcuts import render
from models import *


# Class for listing user's friends
def get_list_of_friends(self, request, user_id):
    user = User.objects.get(id=user_id)
    user_friends = user.get_friends
    resp = {}
    for f in user_friends:
        friend = {
            'name': f.name,
            'location': f.location,
            'image': f.img_url
        }
        self.resp.update(friend)
    return Response(resp)
