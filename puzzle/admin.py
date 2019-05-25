from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(puzzle)
admin.site.register(hint_password)
admin.site.register(wrong_page)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'answer_content', 'answer_created_by', 'answer_created_time']
    search_fields = ['answer_content', 'answer_created_by', 'answer_created_time']


admin.site.register(Answer, AnswerAdmin)
