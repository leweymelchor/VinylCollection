from django.contrib import admin
from .models import Record, Artist, USER_MODEL

# Register your models here.
admin.site.register(Record)
admin.site.register(Artist)

class RecordAdmin(admin.ModelAdmin):
    list_filter = ('owner__username')
