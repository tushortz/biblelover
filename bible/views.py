from django.shortcuts import render


def index(request):
    return render(request, 'bible/index.html')


def book(request, book):
    context = {
        "book": book
    }

    return render(request, 'bible/book.html', context)


def chapter(request, book, chapter):
    verses = ["yes", "lad", "how"]

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
