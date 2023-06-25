from app.models import Subscription
from django import forms
from django.utils.translation import gettext_lazy as _


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = '__all__'
        error_messages = {
            'first_name': {
                'required': _('First name is Must')
            }
        }
