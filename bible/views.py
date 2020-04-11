from django.shortcuts import render
from bible.models import Bible


def index(request):
    return render(request, 'bible/index.html')


def book(request, book):
    book = Bible.objects.filter(book__iexact = book)
    chapters = book.order_by('chapter').values('chapter').distinct()

    context = {
        "chapters": chapters,
        "book": book.first()
    }

    return render(request, 'bible/book.html', context)


def chapter(request, book, chapter):
    verses = Bible.objects.filter(book__iexact = book, chapter=chapter).order_by('chapter')

    context = {
        "book": book,
        "chapter": chapter,
        "verses": verses
    }
    return render(request, 'bible/chapter.html', context)


def verse(request, book, chapter, verse):
    context = {
        "book": book,
        "chapter": chapter,
        "verse": verse,
        "text": "hello"
    }
    return render(request, 'bible/verse.html', context)


def search(request):
    results = ["this", "is", "a", "test"]
    context = {
        "results": results
    }

    return render(request, 'bible/search.html', context)
