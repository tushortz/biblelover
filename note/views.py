from django.shortcuts import render
from note.models import Note
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    notes = Note.objects.filter(author_id=request.user.id)

    context = {
        "notes": notes
    }
    return render(request, 'note/index.html')

@login_required
def show(request, uuid):
    note = Note.objects.get(uuid=uuid, author_id=request.user.id)
    
    context = {
        "note": note
    }

    return render(request, 'note/show.html', context)


@login_required
def community_feeds(request):
    notes = Note.objects.get(visible=True).order_by("-created_on")[:15]
    
    context = {
        "note": notes
    }

    return render(request, 'note/show.html', context)
