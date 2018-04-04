from django.forms import ModelForm
from . import models


class MyForm(ModelForm):
    class Meta:
        model = models.Item
        fields = ['description', 'done']
