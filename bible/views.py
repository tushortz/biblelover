from django.shortcuts import render
from bible.models import Bible
from django.contrib.auth.decorators import login_required


def index(request):
    old_books = Bible.objects.filter(category="old").order_by('category').values('book').distinct()
    new_books = Bible.objects.filter(category="new").order_by('category').values('book').distinct()

    context = {
        "old_books": old_books,
        "new_books": new_books
    }

    return render(request, 'bible/index.html', context)


def book(request, book):
    book = Bible.objects.filter(book__iexact=book)
    chapters = book.order_by('chapter').values('chapter').distinct()

    context = {
        "chapters": chapters,
        "book": book.first()
    }

    return render(request, 'bible/book.html', context)


def chapter(request, book, chapter):
    book = Bible.objects.filter(
        book__iexact=book, chapter=chapter)
    verses = book.order_by('verse')

    context = {
        "book": book.first(),
        "chapter": chapter,
        "verses": verses
    }
    return render(request, 'bible/chapter.html', context)


def verse(request, book, chapter, verse):
    book = Bible.objects.get(book__iexact=book, chapter=chapter, verse=verse)

    context = {
        "book": book
    }
    return render(request, 'bible/verse.html', context)


def search(request):
    results = ["this", "is", "a", "test"]
    context = {
        "results": results
    }

    return render(request, 'bible/search.html', context)


@login_required
def quiz(request):
    context = {}
    return render(request, 'bible/quiz.html', context)
