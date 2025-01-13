from django.forms import ModelForm
from .models import CHECKING

class CheckingForm(ModelForm):
    class Meta:
        model = CHECKING
        fields = ['date', 'chck']