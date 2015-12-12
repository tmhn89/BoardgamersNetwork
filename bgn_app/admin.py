from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Event)
admin.site.register(Guild)
admin.site.register(Participant)
admin.site.register(GuildMember)