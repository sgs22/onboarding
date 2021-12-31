from django.contrib import admin

from django.contrib import admin

from .models import Question, Quiz, Choice

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)

