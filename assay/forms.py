from django import forms
from .models import Answer


class AnswerForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        required=True,
        empty_label=None,
        widget=forms.CheckboxSelectMultiple,
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
