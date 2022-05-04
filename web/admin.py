from django.contrib import admin

# Register your models here.

from . models import Funfact, Scale, Tip, Post, Link, Photo

admin.site.register(Funfact)
admin.site.register(Scale)
admin.site.register(Tip)
admin.site.register(Post)
admin.site.register(Link)
admin.site.register(Photo)




