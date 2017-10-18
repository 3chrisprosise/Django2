from django.contrib import admin
from . import models
# Register your models here.

# admin.site.register(models.Choice)
# ''':type 0'''
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pubdate', 'question_text']
#
# admin.site.register(models.Question, QuestionAdmin)

''':type 1'''
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question_Text',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pubdate']}),
    ]

    list_filter = ['pubdate']

    search_fields = ['question_text']

    list_display = ('question_text', 'pubdate', 'was_published_recently')
admin.site.register(models.Question, QuestionAdmin)

# ''':type 2'''
# class ChoiceInline(admin.StackedInline):
#     model = models.Choice
#     extra = 3
#
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#
# admin.site.register(models.Question, QuestionAdmin)
#
#
# ''' :type 3'''
#
# class ChoiceInline(admin.TabularInline):
#     model = models.Choice
#     extra = 3
#
#
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#
# admin.site.register(models.Question, QuestionAdmin)
