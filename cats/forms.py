import datetime

from django import forms


from cats.models import Cat, Parent


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['style'] = 'color: black;'


class CatForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Cat
        fields = '__all__'

    def clean_dob(self):
        cleaned_data = self.cleaned_data['dob']
        now_year = datetime.datetime.now().year
        if now_year - cleaned_data.year > 100:
            raise forms.ValidationError('собака должна быть моложе 100 лет')
        return cleaned_data



class ParentForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'
