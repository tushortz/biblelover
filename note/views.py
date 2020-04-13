from django.shortcuts import render
from note.models import Note
from django.contrib.auth.decorators import login_required
from bible.models import Bible


@login_required
def index(request):
    """
    Show a list of all the user notes
    """

    data = request.GET.dict()
    book = data.get("book")
    chapter = data.get("chapter", 1)

    notes = Note.objects.filter(author_id=request.user.id)

    if book and chapter:
        verses = Bible.objects.filter(
            book__iexact=book, chapter=chapter)
        notes = notes.filter(verses__in=verses)

    notes.order_by("-created_on")[:15]

    context = {
        "notes": notes
    }
    return render(request, 'note/index.html')


@login_required
def show(request, uuid):
    """
    Show one user note filtered by its UUID
    """
    note = Note.objects.get(uuid=uuid, author_id=request.user.id)

    context = {
        "note": note
    }

    return render(request, 'note/show.html', context)


@login_required
def community_feeds(request):
    """
    Show a list of all the notes set to public by everyone in the community
    """

    book = request.GET

    notes = Note.objects.filter(public=True)

    if book and chapter:
        verses = Bible.objects.filter(
            book__iexact=book, chapter=chapter)
        notes = notes.filter(verses__in=verses)

    notes.order_by("-created_on")[:15]

    context = {
        "notes": notes
    }

    return render(request, 'note/community.html', context)
