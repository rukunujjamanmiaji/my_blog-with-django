from django import forms
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    password = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='re type password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        cd =self.cleaned_data

        if cd['password']!= cd['password2'] :
            raise forms.ValidationError("password don't match")
        return cd['password2']
