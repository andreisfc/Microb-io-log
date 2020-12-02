__name__ = 'fcautils'

def populate_db(numposts=1):
    from django.contrib.auth.models import User
    from lorem import get_paragraph
    from random import choice
    from django.template.defaultfilters import slugify

    authors = User.objects.all()
    organisms = ["Bacillus anthracis", "Escherichia coli", "Helicobacter pylori"]

    postcount = Post.objects.count()

    for i in range(numposts):
        p = Post(
            title = f"Titulo temporario {postcount+i+1}",
            author = choice(authors).username,
            creationdate = timezone.now(),
            updatedate = timezone.now(),
            organism = choice(organisms),
            text = get_paragraph(count=choice(range(5,10)),sep='<br>'),
        )
        p.save()

def clear_db():
    tmp = Post.objects.all()
    for i in tmp:
        i.delete()