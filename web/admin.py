from django.contrib import admin

from web.models import Word,WordMeaning


class AdminWord(admin.ModelAdmin):
    list_display = ["word",]

admin.site.register(Word,AdminWord)

class AdminWordMeaning(admin.ModelAdmin):
    list_display = ( "get_wordname","meaning",'synonyms', 'examples')

    def get_wordname(self, instance):
        return instance.word.word

admin.site.register(WordMeaning,AdminWordMeaning)