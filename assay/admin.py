from django.contrib import admin

from .models import Group, Question, Test, Answer


class GroupAdmin(admin.ModelAdmin):
    list_display = ("group_name",)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("test", "question", "answer", "truth")


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text",)


admin.site.register(Group, GroupAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Test)
