from django import template
from records.models import Record
from django.db.models import Sum

register = template.Library()

@register.simple_tag
def total_tag(user):
    owner = user
    records = Record.objects.filter(owner=owner)
    total = records.aggregate(total=Sum('price'))['total']

    if total is None:
        total = 0

    total = total

    def format_with_commas(number):
        parts = f"{number:,.2f}".split(".")
        return ".".join(parts)

    number = total
    formatted_number = format_with_commas(number)
    return formatted_number
