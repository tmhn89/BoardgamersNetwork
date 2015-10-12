from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

import requests
import xml.etree.ElementTree as ET
import xmltodict

from .models import *

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

def users(request):
    users = User.objects.order_by('-name')[:5]

    # output = "<table>"
    # for user in users:
    #     output += "<tr class='usr'>"
    #     output += "<td>" + user.name + "</td>"
    #     output += "<td>" + user.email + "</td>"
    #     output += "<td>" + user.location + "</td>"
    #     output += "<td><img src='" + user.img_url + "' height='50'/></td>"
    #     output += "</tr>"

    # output += "</table>"    

    # return HttpResponse(output)

    template = loader.get_template('users.html')
    context = RequestContext(request, {
        'users': users,
    })

    return HttpResponse(template.render(context))

def games(request):
    # games = User.objects.order_by('-name')[:3]

    template = loader.get_template('games.html')
    # context = RequestContext(request, {
    #     'games': games,
    # })
    # print(context)
    r = requests.get('https://www.boardgamegeek.com/xmlapi/collection/irkinvader')
    #print(r.text)
    data = xmltodict.parse(r.text)
    #tree = ET.parse(r.text)
    #root = tree.getroot()
    #print(tree)
    context = RequestContext(request, {
        'games': data
    })

    return HttpResponse(template.render(context))

