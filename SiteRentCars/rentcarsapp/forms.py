from .models import *
from django import forms


class RentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['CarName'].empty_label="Машина не выбрана"
    class Meta:
        model = RentModel
        fields = ["name", "mail", "Data", "CarName"]
        widgets = {"name": forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя'
        }),
            "mail": forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите Email'
        }),
            "Data": forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату в формате дд.мм.гггг'
        }),
            "CarName": forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите машину'
        })
        }