from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from .models import User


@login_required
def get_list_of_friends(self, request, user_id):
    """
    Lists user's friends
    """
    user = User.objects.get(id=request.user_id)
    # user should be stored in request
    # user = request.user
    user_friends = user.get_friends()
    resp = []
    for f in user_friends:
        friend = {
            'name': f.name,
            'location': f.location,
            'image': f.img_url
        }
        self.resp.append(friend)

    # resp friend_list = [{'name': 'Annika Oukka', 'location': 'Espoo',
    # 'image': 'http://....'}, {'name': '',..}, {..}]
    return render_to_response(
        'templates/friends/list_friends.html', {
            'friend_list': resp
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


@login_required
def add_friend(self, request, user_id, friend):
    """
    Add friend to user
    """
    user = User.objects.get(id=request.user_id)
    # replace above with user = request.user
    user.add_friend(friend)


@login_required
def remove_friend(self, request, user_id, friend):
    """
    Remove friend from user
    """
    user = User.objects.get(id=request.user_id)
    # replace above with user = request.user
    user.remove_friendship(friend)


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
