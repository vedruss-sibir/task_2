from django.contrib import admin

from .models import Group, Question, Choice, Test


class GroupAdmin(admin.ModelAdmin):
    list_display = ("group_name",)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("test", "question", "answer", "truth")


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("test", "question_text")


admin.site.register(Group, GroupAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Test)
