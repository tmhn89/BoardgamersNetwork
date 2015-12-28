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
    choices = [('0', 'All games are welcomed'), ('15987', 'Arkham Horror'), ('166372', 'Artificium'), ('3955', 'Bang'), ('13', 'Catan'), ('131357', 'Coup'), ('178900', 'Codenames'), ('9446', 'Blue Moon'), ('150376','Dead of Winter'), ('1927', 'Munchkin'), ('125548', 'Pixel Tactics'), ('41114', 'The Resistance'), ('925', 'Werewolf')]
    main_game = forms.MultipleChoiceField(choices=choices, initial={'0': 'All games are welcomed'}, required=False)
    time = forms.TextInput(attrs={'class': 'datetimepicker',})
    description = forms.Textarea()
    participants = forms.ModelMultipleChoiceField(queryset=UserProfile.objects.all(), required=False)

    # def clean(self):
    #     return self.cleaned_data

    def __init__(self, *args, **kwargs):
         self.user = kwargs.pop('user', None)
         super(EventForm, self).__init__(*args, **kwargs)
         self.fields['participants'].queryset = self.fields['participants'].queryset.exclude(id=self.user.userprofile.id)


    class Meta:
        model = Event
        fields = '__all__'        