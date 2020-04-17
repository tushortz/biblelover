from django import template

register = template.Library()


@register.filter(name='urlify_verse')
def urlify_verse(verses):
    data = {}

    for v in verses:
        v.verse = str(v.verse)

        if not data.get(v.book):
            data[v.book] = dict()

        if not data.get(v.book).get(v.chapter):
            data[v.book][v.chapter] = set()

        data[v.book][v.chapter].add(v.verse)

    books = []
    text = ""
    
    for book, key in data.items():
        for chapter, verse in sorted(key.items()):
            if book in books:
                book = ","
            else:
                books.append(book)
            
            text += (f"{book} {(chapter)}:{','.join(sorted(verse))}")
        text += ", "

    return text.rstrip(", ")
