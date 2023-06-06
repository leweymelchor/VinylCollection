from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Sign Up Form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

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

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            ]

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
                "price"
            ]

    class ArtistForm(forms.ModelForm):
        class Meta:
            model = Artist
            fields = [
                "artist"
            ]

except Exception:
    pass
