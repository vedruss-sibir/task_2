from django.contrib import admin

from .models import Group, Question, Choice


class GroupAdmin(admin.ModelAdmin):
    list_display = ("group_name",)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("group_name",)


admin.site.register(Group, GroupAdmin)
admin.site.register(Question)
admin.site.register(Choice)
