from .models import Theme
from django.forms import ModelForm

class ThemeForm(ModelForm):
    class Meta:
        model = Theme
        fields = ('theme_name',)

    def clean(self):
        name = self.cleaned_data['theme_name']
        words_list = name.split()

        while len(name) > 30:
            last_word = words_list.pop()
            name = name[:len(name)-len(last_word)-1]

        self.cleaned_data['theme_name_url'] = '_'.join(words_list)
        return self.cleaned_data
