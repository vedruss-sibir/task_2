from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError


from .models import Group, Question, Test, Answer

tr = 0


class Answer_Valide_Form(forms.ModelForm):
    class Meta:
        model = Answer
        fields = (
            "answer",
            "truth",
        )

    def clean(self):
        global tr
        tru = self.cleaned_data["truth"]
        if tru:
            tr = tr + 1
            if tr > 1:
                tr = 0
                raise ValidationError("Выбирете только один верный ответ")
        #   if tr == 0:
        #      raise ValidationError("Выбирете один верный ответ!!!")
        return self.cleaned_data


class ChoiceInline(admin.StackedInline):
    form = Answer_Valide_Form
    model = Answer
    extra = 3


class GroupAdmin(admin.ModelAdmin):
    list_display = ("group_name",)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("test", "question_text")
    inlines = [ChoiceInline]


##   list_display = ("test", "answer", "truth")


admin.site.register(Group, GroupAdmin)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Answer, AnswerAdmin)
admin.site.register(Test)
