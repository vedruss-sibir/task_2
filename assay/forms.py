from django import forms
from .models import Choice


class ChoiceForm(forms.ModelForm):
    class Meta:
        # На основе какой модели создаётся класс формы
        model = Choice
        # Укажем, какие поля будут в форме
        fields = ("question", "answer")
