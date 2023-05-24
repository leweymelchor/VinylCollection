from django import forms
try:
    from records.models import Record

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

except Exception:
    pass
