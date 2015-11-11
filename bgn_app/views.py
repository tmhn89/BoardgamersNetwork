from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from .models import User, Event, Participants, Guild
import json as simplejson

import requests
import xmltodict

from .models import *

def event(self):

    data = [
        {
            'name': 'GameDay',
            'coordinates': [60.186455, 24.837126],
            'address': 'Jamerantaival 1',
            'image_url': 'https://theromanticvineyard.files.wordpress.com/2013/01/clue-board.jpg',
            'attendee_count': 9,
            'description': 'Lorem ipsum dolor sit amet, non numquam proinmae.'
        },
        {
            'name': 'Otaniemi Gaming Night',
            'coordinates': [60.186555, 24.837138],
            'address': 'Otakaari 20',
            'image_url': 'http://d1mvvfdyo8jq4k.cloudfront.net/media/susd/images/2013/7/28/c6138082f7ce11e28594f23c91709c91_1375047823.jpg',
            'attendee_count': 16,
            'description': 'Lorem ipsum dolor sit amet, non numquam proinmae.'
        },
        {
            'name': 'Dominion',
            'coordinates': [60.186457, 24.837121],
            'address': 'Konemiehentie 1',
            'image_url': 'http://thisisinfamous.com/wp-content/uploads/2014/06/dominion-1.jpg',
            'attendee_count': 4,
            'description': 'Lorem ipsum dolor sit amet, non numquam proinmae.'
        },
    ]

    return render_to_response(
        'location/map.html', {
            'events': data
        }
    )


@login_required
def list_of_user_matches(self, request, user_id):
    """
    List user's matches. Matches are people who share
    the same interests and nearby location with the user
    """

    # return render_to_response(
    #     'templates/friends/list_user_matches.html', {
    #         'friend_list': resp
    #     }
    # )
    pass

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

def guild_detail(request):
    guild_id = 1
    guild = Guild.objects.get(id=guild_id)
    
    guild_member =[3,4,5,7]
    guild_event =[1,2]
    member_list = []
    event_list = []
    for mid in guild_member:
        this_member = User.objects.get(id=mid)
        member_list.append({'name': this_member.name, 'email':this_member.email, 'img_url': this_member.img_url, 'location': this_member.location})
    for eid in guild_event:
        this_event = Event.objects.get(id=eid)
        event_list.append({'venue': this_event.venue, 'time':this_event.time, 'host': this_event.host, 'main_game': this_event.main_game, 'description': this_event.description})

    print(member_list)
    template = loader.get_template('guild_detail.html')
    context = RequestContext(request, { 
        'guild': guild,
        'members': member_list,
        'events': event_list
    })

    return HttpResponse(template.render(context))

def event_detail(request):
    event_id = 1;
    event = Event.objects.get(id=event_id)
    #partcipants = Partcipants.objects.get(event=event_id)
    participants = [1,2,3,4,5]
    participants_list = []
    for pid in participants:
        this_participant = User.objects.get(id=pid)
        participants_list.append({'name': this_participant.name, 'email':this_participant.email, 'img_url': this_participant.img_url, 'location': this_participant.location})

    event_info ={
        'name':'EVENT name',
        'description':'this is just an example description.this is just an example description.this is just an example description.this is just an example description.this is just an example description.this is just an example description.this is just an example description.',
        'game_list':'example games',
        'host':'john doe',
        'location':'a location',
        'date':'a date',
        'image':'blabla',
        'participants_list':[1,2,3,4,5],
    }
    template = loader.get_template('event_detail.html')
    data = event_info;
    context = RequestContext(request, { 
        'event_detail': event,
        'participants': participants_list,
        'host': event.host
    })

    return HttpResponse(template.render(context))
