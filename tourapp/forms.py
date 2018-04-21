from django.forms import ModelForm
from tourapi.models import Tourism

class TourismForm(ModelForm):
    class Meta:
        model = Tourism
        fields = ['destination', 'tourist']