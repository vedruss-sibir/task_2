from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Answer


User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email")


class AnswerForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        widget=forms.RadioSelect,
        queryset=None,
    )

    class Meta:
        model = Answer
        fields = ("answer",)

    def __init__(self, *args, **kwargs):
        question = kwargs.pop("question")
        qs = Answer.objects.filter(question=question)
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields["answer"].queryset = qs
