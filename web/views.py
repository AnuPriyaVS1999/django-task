from django.shortcuts import render,get_object_or_404,redirect

from web.models import Word, WordMeaning


def index(request):
    if request.method == 'POST':
        search_word = request.POST.get('search_word')
        word = Word.objects.filter(word=search_word)
        error_msg = False
        error = "The word '{}' is not found"

        if word:
            word_meaning = WordMeaning.objects.filter(word__in=word).order_by('priority')
            context = {
                "title": "Dictionary",
                "meanings": word_meaning,
                "word": search_word,
                "show": True,
            }
            return render(request, 'web/index.html', context)

        elif search_word == '':
            error_msg="Empty Search"
            context = {
                "title": "Dictionary",
                "word": search_word,
                "show": True,
                "error_msg": error_msg,
            }
            return render(request, 'web/index.html', context)
            
        else:
            error_msg = error.format(search_word)
            word_meaning = ""

            context = {
                "title": "Dictionary",
                "word": search_word,
                "show": True,
                "error_msg": error_msg,
            }
            return render(request, 'web/index.html', context)

    else:
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
        if new_word:
            WordMeaning.objects.create(
                word=new_word,
                meaning=meaning,
                priority=priority,
            )

    context = {
        "title": "Adding word to dictionary"
    }
    return render(request, "web/addword.html", context)





def edit_word(request,id):
    word_list = Word.objects.filter(is_delete=False, is_edit=False)
    edit_list = Word.objects.filter(is_edit=False,is_delete=False)
    instance = get_object_or_404(Word,id=id)
    if request.method == 'POST':
        edited_text = request.POST.get("edited-text")
        instance = Word.objects.get(id=id)
        if edited_text :
            instance.title = edited_text
            instance.save()

        return redirect("web:index.html")
    context = {
        "title": "",
        "word_list": word_list,
        "edit_list": edit_list,
        'word_text':instance
    }
    return render(request, "web/edit.html", context=context)
