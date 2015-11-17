from django import forms
from .models import *
import datetime
from django.utils import timezone

class UserForm(forms.ModelForm):
    """
    Form for creating user
    """


class EventForm(forms.ModelForm):
    """
    Form for creating event
    """
    choices = [('15987', 'Arkham Horror'), ('166372', 'Artificium'), ('9446', 'Blue Moon')]
    main_game = forms.MultipleChoiceField(choices=choices)
    class Meta:
        model = Event
        fields = '__all__'