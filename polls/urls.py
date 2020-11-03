from django.urls import path

from . import views

# routes with URL patterns
urlpatterns = [
    path('', views.index, name='index'),
    path('page', views.page, name='page')
]
