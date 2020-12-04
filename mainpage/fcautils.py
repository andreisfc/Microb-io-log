def populate_db(numposts=1):
    from lorem import get_paragraph, get_sentence
    from random import choice

    authors = User.objects.all()
    orgs = Organism.objects.all()

    for i in range(numposts):
        p = Post(
            title = get_sentence(),
            author = choice(authors),
            organism = choice(orgs),
            text = get_paragraph(count=choice(range(5,10))),
        )
        p.save()

def update_posts():
    from random import choice

    p = Post.objects.all()
    l = choice(range(len(p)))

    for i in range(l):
        choice(p).save()

def clear_db():
    tmp = Post.objects.all()
    for i in tmp:
        i.delete()