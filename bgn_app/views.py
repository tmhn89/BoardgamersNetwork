from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

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