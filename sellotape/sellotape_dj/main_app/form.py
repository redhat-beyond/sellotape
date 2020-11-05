from django.forms import ModelForm
from .models import Stream


class StreamForm(ModelForm):
    class Meta:
        model = Stream
        exclude = (['author', 'added_on', ])  # this says to include all fields from model to the form