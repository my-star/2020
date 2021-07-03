from django import forms

class UserLogin(forms.Form):
    emp_num = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)