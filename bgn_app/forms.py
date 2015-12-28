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
    choices = [(u'', 'Choose games'), ('15987', 'Arkham Horror'), ('166372', 'Artificium'), ('9446', 'Blue Moon')]
    main_game = forms.MultipleChoiceField(choices=choices, initial={u'': 'Choose games'})
    time = forms.TextInput(attrs={'class': 'datetimepicker',})
    description = forms.Textarea()
    participants = forms.ModelMultipleChoiceField(queryset=UserProfile.objects.all())

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