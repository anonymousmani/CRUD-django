from django import forms
from enroll.models import user

class userform(forms.ModelForm):
    class Meta:
        model = user
        fields = ['name', 'email', 'password']
        ''' widget = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.TextInput(attrs={'class':'form-control'}),}
        '''