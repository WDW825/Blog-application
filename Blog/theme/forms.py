from .models import Theme
from django.forms import ModelForm

class ThemeForm(ModelForm):
    class Meta:
        model = Theme
        fields = ('theme_name',)

