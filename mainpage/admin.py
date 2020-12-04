from django.contrib import admin
from mainpage.models import Post, Organism

class OrgAdmin(admin.ModelAdmin):
    fields = [
        "name"
    ]

class PostAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "organism",
        "text"
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Organism, OrgAdmin)