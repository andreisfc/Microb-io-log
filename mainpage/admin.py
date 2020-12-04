from django.contrib import admin
from django.contrib.auth.models import User
from mainpage.models import Post, Organism

class OrgAdmin(admin.ModelAdmin):
    fields = [
        "name"
    ]

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'creationdate', 'updatedate')
    fields = [
        "title",
        "organism",
        "text"
    ]


admin.site.site_header = 'Microb[io]log[y] Command Center'
admin.site.register(Post, PostAdmin)
admin.site.register(Organism, OrgAdmin)