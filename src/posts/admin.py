from django.contrib import admin

# Register your models here.

from .models import Form, Post

admin.site.register(Post)
admin.site.register(Form)