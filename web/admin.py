from django.contrib import admin

from web.models import Word,Meaning


class AdminWord(admin.ModelAdmin):
    list_display = ("word")

admin.site.register(Word)

class AdminMeaning(admin.ModelAdmin):
    list_display = ["word","meaning","example","synonyms"]

admin.site.register(Meaning,AdminMeaning)