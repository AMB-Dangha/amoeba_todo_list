from django import template
from django.utils import timezone

register = template.Library()


@register.filter
def pretty_date(value):
    today = timezone.now().date()
    if value == today:
        return 'Today'
    elif value == today - timezone.timedelta(days=1):
        return 'Yesterday'
    else:
        return value
