from django import forms
from chat.models import Thread

class ChatForm(forms.Form):
    class Meta:
        #my_field = forms.CharField()
        model = Thread
        fields = ['first_person', 'second_person']