from django.urls import path
from . import views
print ('Urls.py')
urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('directors/', views.director_list, name='director_list'),
    path('movies/<int:pk>', views.movie_detail, name='movie_detail'),
    path('directors/<int:pk>', views.director_detail, name='director_detail'),
    path('directors/new', views.director_create, name='director_create'),
]