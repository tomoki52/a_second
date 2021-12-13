from django.forms import ModelForm, fields
from django.forms.models import model_to_dict
from .models import Clock

class ClockForm(ModelForm):
    class Meta:
        model = Clock
        fields = ["second"]