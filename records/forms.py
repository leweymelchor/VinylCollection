from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Artist, Record

from django.forms.widgets import NumberInput

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


class RecordForm(forms.ModelForm):
    album = forms.CharField(initial='Album Title Here', max_length=100, required=True)
    artwork = forms.CharField(initial='URL link to album art', max_length=300)
    artist = forms.ModelChoiceField(
        queryset = Artist.objects.all(),
        initial = 0
        )
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    price = forms.DecimalField(initial=20.00)

    class Meta:
        model = Record
        fields = (
            "album",
            "artwork",
            "artist",
            "date",
            "price",
        )

        widgets = {
            'album': forms.TextInput(attrs={'class': 'form-artist'}),
            'artwork': forms.TextInput(attrs={'class': 'form-artist'}),
            'artist': forms.TextInput(attrs={'class': 'form-artist'}),
            'date': forms.TextInput(attrs={'class': 'form-artist'}),
            'price': forms.TextInput(attrs={'class': 'form-artist'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(RecordForm, self).__init__(*args, **kwargs)
        self.fields['artist'].queryset = Artist.objects.filter(owner_id=self.request.user)

    def save(self, commit=True):
        instance = super(RecordForm, self).save(commit=False)
        if self.request:
            instance.owner = self.request.user
        if commit:
            instance.save()
        return instance


class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = [
            "artist",
        ]
