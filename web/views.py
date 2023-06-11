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
        synonyms = request.POST.get('word_synonyms')
        examples = request.POST.get('word_examples')

        new_word, created = Word.objects.get_or_create(
            word=word
        )
        if created:
            WordMeaning.objects.create(
                word=new_word,
                meaning=meaning,
                synonyms=synonyms,
                examples=examples,
                priority=priority,
            )
            redirect('/')

    context = {
        "title": "Adding word to dictionary"
    }
    return render(request, "web/addword.html", context)


def edit_word(request, pk):
    word_instance = Word.objects.get(id=pk)
    if word_instance:
        if WordMeaning.objects.filter(word=word_instance).exists():
            word_meaning_instance = WordMeaning.objects.get(word=word_instance)

    
    
    if request.method == "POST":
        word = request.POST.get("edited-text")
        meaning = request.POST.get("edited-word-meaning")
        priority = request.POST.get('priority')
        synonyms = request.POST.get('edited-word-synonyms')
        examples = request.POST.get('edited-word-examples')
        print(meaning)
        print(word)
        
        
        if word:
            word_instance.word = word
            word_meaning_instance.meaning=meaning
            word_meaning_instance.priority=priority
            word_meaning_instance.synonyms=synonyms
            word_meaning_instance.examples=examples
            word_meaning_instance.save()
         

        return redirect('/')  # Assuming you have a word_detail view

    context = {
        "title": "Edit Page",
        "word_meaning_instance": word_meaning_instance,
        "word_instance": word_instance,
        "word_id": pk
    }
    return render(request, "web/edit.html", context)