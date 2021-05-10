from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index, name = 'index'),
    path('analyze', analyze, name = 'analyze'),
    # path('capitalizefirst', capfirst, name = 'capfirst'),
    # path('newlineremove',newlineremove , name = 'newlineremove'),
    # path("spaceremove", spaceremove, name = 'spaceremove'),
    # path('charcount',charcount, name = 'charcount'),
]
