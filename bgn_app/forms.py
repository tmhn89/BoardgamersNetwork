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
    choices = [('0', 'All games are welcomed'), ('15987:Arkham Horror', 'Arkham Horror'), ('166372:Artificium', 'Artificium'), ('3955:Bang', 'Bang'), ('13:Catan', 'Catan'), ('131357:Coup', 'Coup'), ('178900:Codenames', 'Codenames'), ('9446:Blue Moon', 'Blue Moon'), ('150376:Dead of Winter','Dead of Winter'), ('2580:Dominion', 'Dominion'), ('1927:Munchkin', 'Munchkin'), ('125548:Pixel Tactics', 'Pixel Tactics'), ('41114:The Resistance', 'The Resistance'), ('925:Werewolf', 'Werewolf')]
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


class UpdateUserProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = UserProfile
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'email', 'location'
        )

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
