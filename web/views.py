from django.shortcuts import render, get_object_or_404, redirect
from web.models import Word, WordMeaning

def index(request):
    if request.method == 'POST':
        search_word = request.POST.get('search_word')
        error_msg = False
        error = "The word '{}' is not found"
        
        if search_word == '':
            error_msg = "Empty Search"
            context = {
                "title": "Dictionary",
                "word": search_word,
                "show": True,
                "error_msg": error_msg,
            }
            return render(request, 'web/index.html', context)
            
        word = Word.objects.filter(word=search_word)
        if word:
            word_meaning = WordMeaning.objects.filter(word__in=word).order_by('priority')
            word=Word.objects.filter(word=search_word)
            context = {
                "title": "Dictionary",
                "meanings": word_meaning,
                "word": search_word,
                "show": True,
                "words":word
            }
            return render(request, 'web/index.html', context)
        
        error_msg = error.format(search_word)
        context = {
            "title": "Dictionary",
            "word": search_word,
            "show": True,
            "error_msg": error_msg,
        }
        return render(request, 'web/index.html', context)
    
    context = {
        "title": "Dictionary",
        "searchword": "",
        "word": "",
        "show": False,
    }
    return render(request, 'web/index.html', context)


def create_word(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        meaning = request.POST.get('word_meaning')
        priority = request.POST.get('priority')

        new_word, created = Word.objects.get_or_create(
            word=word
        )
        if created:
            WordMeaning.objects.create(
                word=new_word,
                meaning=meaning,
                priority=priority,
            )

    context = {
        "title": "Adding word to dictionary"
    }
    return render(request, "web/addword.html", context)


def edit_word(request, id):
    word_instance = Word.objects.get(id=id)
    word_meaning_instance = WordMeaning.objects.filter(word=word_instance)

    
    
    if request.method == "POST":
        word = request.POST.get("edited-word")
        meaning = request.POST.get("edited-meaning")
        print(meaning)
        
        
        if word:
            word_instance.word = word
        for meaning in word_meaning_instance:
            meaning.meaning=meaning
            meaning.save()
        word_instance.save()

        return redirect('word_detail', id=id)  # Assuming you have a word_detail view

    context = {
        "title": "Edit Page",
        "word_meaning_instance": word_meaning_instance,
        "word_instance": word_instance,
        "word_id": id
    }
    return render(request, "web/edit.html", context)
