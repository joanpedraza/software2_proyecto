from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password1']




    def __init__(self, *args, **kwargs):
        super(CustomRegisterForm, self).__init__(*args, **kwargs)
        
        # Añadir clases de Tailwind a cada campo
        self.fields['username'].widget.attrs.update({
            'class': 'w-full p-3 border border-gray-300 rounded-md placeholer:font-light',
            'placeholder': 'Username'
        })

        self.fields['first_name'].widget.attrs.update({
            'class': 'w-full p-3 border border-gray-300 rounded-md placeholer:font-light',
            'placeholder': 'First Name'
        })

        self.fields['last_name'].widget.attrs.update({
            'class': ' w-full p-3 border border-gray-300 rounded-md placeholder:font-light',
            'placeholder': 'Last name'
        })

        self.fields['email'].widget.attrs.update({
            'class': ' w-full p-3 border border-gray-300 rounded-md placeholder:font-light',
            'placeholder': 'Email'
        })

        self.fields['password1'].widget.attrs.update({
            'class': ' w-full p-3 border border-gray-300 rounded-md placeholder:font-light',
            'placeholder': 'password'
        })

       


        

