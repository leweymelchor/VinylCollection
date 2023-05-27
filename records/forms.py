from django import forms
try:
    from records.models import Artist, Record

    class RecordForm(forms.ModelForm):
        class Meta:
            model = Record
            fields = [
                "artist",
                "album",
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
