from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from .models import User, Event
import json as simplejson


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
