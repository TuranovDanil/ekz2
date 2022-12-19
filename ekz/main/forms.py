from django import forms

from .models import Product


class CreateForm(forms.ModelForm):
    name = forms.CharField(label='Название')
    desc = forms.CharField(label='Описание')
    photo = forms.ImageField(label='Фото')

    class Meta:
        model = Product
        fields = ('name', 'desc', 'photo')
        enctype = "multipart/form-data"