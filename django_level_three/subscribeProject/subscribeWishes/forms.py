from django import forms
from subscribeWishes.models import Customer

class NewSubscriber(forms.ModelForm):
    class Meta():
        model = Customer
        fields = '__all__'