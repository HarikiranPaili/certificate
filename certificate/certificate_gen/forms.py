from django import forms
from .models import *

class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event_details
        fields = ('__all__')