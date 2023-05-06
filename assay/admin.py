from django.contrib import admin

from .models import Group, Question, Test, Answer


class ChoiceInline(admin.StackedInline):
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
