from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SingUpForm(UserCreationForm):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            "type":"text",
            "name":"first_name",
            "class":"form-control",
            "required":"",
        })

        self.fields['last_name'].widget.attrs.update({
            "type":"text",
            "name":"last_name",
            "class":"form-control",
            "required":"",
        })

        self.fields['username'].widget.attrs.update({
            "type":"text",
            "name":"username",
            "class":"form-control",
            "required":"",
        })

        self.fields['email'].widget.attrs.update({
            "type":"text",
            "name":"email",
            "class":"form-control",
            "required":"",
        })

        self.fields['password1'].widget.attrs.update({
            "type":"text",
            "name":"password1",
            "class":"form-control",
            "required":"",
        })

        self.fields['password2'].widget.attrs.update({
            "type":"text",
            "name":"password2",
            "class":"form-control",
            "required":"",
        })


    
    
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)