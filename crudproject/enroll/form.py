from django import forms
from enroll.models import user

class userform(forms.ModelForm):
    class Meta:
        model = user
        fields = ['id', 'name', 'email', 'password']
        widget = {
            'id' : forms.NumberInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
            }
        