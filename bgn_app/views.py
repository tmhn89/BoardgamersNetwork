from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile, Event, Participant, Guild, GuildMember

import requests
import xmltodict
from .models import *
from .forms import *


class Events():

    def get_events(self):
        # Function for retrieveing all events near the user

        events = [
            {
                'id': 1,
                'name': 'GameDay',
                'coordinates': [60.18775, 24.82846],
                'address': 'Jamerantaival 1',
                'image_url': 'https://theromanticvineyard.files.wordpress.com/2013/01/clue-board.jpg',
                'attendee_count': 9,
                'description': 'Lorem ipsum dolor sit amet, non numquam proinmae.',
                'main_game': 'Game of Thrones'
            },
            {
                'id': 2,
                'name': 'Otaniemi Gaming Night',
                'coordinates': [60.18345, 24.78526],
                'address': 'Otakaari 20',
                'image_url': 'http://d1mvvfdyo8jq4k.cloudfront.net/media/susd/images/2013/7/28/c6138082f7ce11e28594f23c91709c91_1375047823.jpg',
                'attendee_count': 16,
                'description': 'Lorem ipsum dolor sit amet, non numquam proinmae.',
                'main_game': 'Kimble'
            },
            {
                'id': 3,
                'name': 'Dominion',
                'coordinates': [60.16899, 24.94938],
                'address': 'Konemiehentie 1',
                'image_url': 'http://thisisinfamous.com/wp-content/uploads/2014/06/dominion-1.jpg',
                'attendee_count': 4,
                'description': 'Lorem ipsum dolor sit amet, non numquam proinmae.',
                'main_game': 'Dominion'
            },
        ]

        return events


class Guilds():

    def get_guilds(self):

        guilds = [
            {
                'id': 1,
                'name': 'Best Guild',
                'coordinates': [60.18008, 24.81382],
                'hq': 'Mantyviita 3',
                'image_url': 'http://www.blogcdn.com/wow.joystiq.com/media/2011/04/guild-fireworks-larger.jpg',
                'members': 4,
                'description': 'Lorem ipsum dolor sit amet, non numquam proinmae.'
            },
            {
                'id': 2,
                'name': 'Big Guild',
                'coordinates': [60.172190, 24.947443],
                'hq': 'Other address',
                'image_url': 'http://i.imgur.com/Amf3T7i.png',
                'members': 10,
                'description': 'Lorem ipsum dolor sit amet, non numquam proinmae.'
            },
            {
                'id': 3,
                'name': 'Old Guild',
                'coordinates': [60.16898, 24.94948],
                'hq': 'Some address',
                'image_url': 'https://upload.wikimedia.org/wikipedia/commons/9/95/Rembrandt_-_De_Staalmeesters-_het_college_van_staalmeesters_(waardijns)_van_het_Amsterdamse_lakenbereidersgilde_-_Google_Art_Project.jpg',
                'members': 48,
                'description': 'Lorem ipsum dolor sit amet, non numquam proinmae.'
            },
        ]

        return guilds


class Stores():

    def get_stores(self):

        stores = [
            {
                'name': 'Europe Board Game Store',
                'coordinates': [60.172161, 24.947441],
                'address': 'Unionin katu',
                'image_url': 'http://www.wired.com/wp-content/uploads/blogs/geekdad/wp-content/uploads/2012/09/Alchemy-5.jpg',
                'website': '',
                'description': 'Lorem ipsum dolor sit amet, non numquam proinmae.',
                'store_type': 'Everything'
            },
            {
                'name': 'Card Game Store',
                'coordinates': [60.177390, 24.925768],
                'address': 'Pohjoinen Hesperiankatu',
                'image_url': 'http://www.internationalvillagemall.ca/files/OneShop.JPG',
                'website': '',
                'description': 'Lorem ipsum dolor sit amet, non numquam proinmae.',
                'store_type': 'Card Games'
            },
            {
                'name': 'Game Knight',
                'coordinates': [60.210497, 24.944286],
                'address': 'Makelankatu',
                'image_url': 'http://www.hixxysoft.com/Images/Divinity-II-2.jpg',
                'website': '',
                'description': 'Lorem ipsum dolor sit amet, non numquam proinmae.',
                'store_type': 'All Board Games'
            },
        ]

        return stores


@login_required(login_url='/login/')
def around_me(request):
    # events = Events().get_events()
    # guilds = Guilds().get_guilds()
    events = Event.objects.all()
    guilds = Guild.objects.all()
    stores = Stores().get_stores()

    return render_to_response(
        'location/map.html', {
            'events': events,
            'guilds': guilds,
            'stores': stores,
            # 'user': request.user
        },
        RequestContext(request)
    )


def get_users_events(request):
        events = Event.objects.all()

        return render_to_response(
            'events/list_events.html', {
                'events': events,
            },
            RequestContext(request)
        )


def get_users_guilds(request):
    guilds = Guild.objects.all()

    return render_to_response(
        'guilds/list_guilds.html', {
            'guilds': guilds,
        },
        RequestContext(request)
    )


def users(request):
    users = UserProfile.objects.order_by('-name')[:5]

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


def guild_detail(request, guild_id):
    guild_id = 1
    guild = Guild.objects.get(id=guild_id)

    leaders = GuildMember.objects.filter(is_leader=True).filter(guild=guild_id);
    members = GuildMember.objects.filter(is_leader=False).filter(guild=guild_id);

    template = loader.get_template('guild_detail.html')
    context = RequestContext(request, {
        'guild': guild,
        'members': members,
        'leaders': leaders,
        'events': []
    })

    return HttpResponse(template.render(context))


def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    hosts = Participant.objects.filter(is_host=True).filter(event=event_id)
    participants = Participant.objects.filter(is_host=False).filter(event=event_id)

    template = loader.get_template('event_detail.html')
    context = RequestContext(request, {
        'event_detail': event,
        'participants': participants,
        'hosts': hosts
    })

    return HttpResponse(template.render(context))


def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            games = request.POST['main_game']
            post = form.save(commit=False)
            post.save()
            return redirect('event_detail', post.pk)
    else:
        form = EventForm()
    return render(request, 'event_create.html', {'form': form } )


def profile_info(request):
    print request.user
    print request.user.id
    user = User.objects.get(id=request.user.id)
    user_profile = user.userprofile
    template = loader.get_template('user_profile/profile.html')
    context = RequestContext(request, {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'last_login': user.last_login,
        'date_joined': user.date_joined,
        'location': user_profile.location,
        'lat': user_profile.lat,
        'lng': user_profile.lon
    })
    return HttpResponse(template.render(context))


def update_profile(request):
    args = {}
    if request.method == 'POST':
        form = UpdateUserProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('update_profile_success'))
    else:
        form = UpdateUserProfile()

    args['form'] = form
    return render(request, 'user_profile/profile.html', args)
