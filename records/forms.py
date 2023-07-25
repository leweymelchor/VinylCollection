from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Sign Up Form
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={"placeholder": 'Username'}))
    first_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={"placeholder": 'First Name'}))
    last_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={"placeholder": 'Last Name'}))
    email = forms.EmailField(max_length=254, required=False, widget=forms.TextInput(attrs={"placeholder": 'Enter a valid email address'}))
    password1 = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={"placeholder": 'Secure Password'}))
    password2 = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={"placeholder": 'Re-type Password'}))

    error_css_class = 'error-field'

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            ]


class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={"placeholder": 'Username'}))
    first_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={"placeholder": 'First Name'}))
    last_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={"placeholder": 'Last Name'}))
    email = forms.EmailField(max_length=254, required=False, widget=forms.TextInput(attrs={"placeholder": 'Enter a valid email address'}))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            ]

# class LoginForm(forms.ModelForm):
#     username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={"placeholder": 'Username'}))
#     password = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={"placeholder": 'Password'}))

#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'password',
#             ]

try:
    from records.models import Artist, Record

    class RecordForm(forms.ModelForm):
        class Meta:
            model = Record
            fields = [
                "album",
                "artist",
                "artwork",
                "date",
                "price",
            ]

    class ArtistForm(forms.ModelForm):

        class Meta:
            model = Artist
            fields = [
                "artist",
            ]

except Exception:
    pass
