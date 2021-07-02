from django import forms

class userlogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField()