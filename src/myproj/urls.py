from django.contrib import admin
from django.urls import path
 
 
from posts.views import form, header, post_list_view, result, stats
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',post_list_view),
    path('form/',form),
    path('result/',result),
    path('header/',header),
    path('stats/',stats),
]
