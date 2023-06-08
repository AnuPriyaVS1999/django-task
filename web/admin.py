from django.contrib import admin

from web.models import Word,WordMeaning


class AdminWord(admin.ModelAdmin):
    list_display = ("word")

admin.site.register(Word)

class AdminWordMeaning(admin.ModelAdmin):
    list_display = ["word","meaning"]

admin.site.register(WordMeaning,AdminWordMeaning)