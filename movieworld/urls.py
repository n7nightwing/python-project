from django.urls import path
from . import views
print ('Urls.py')
urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movies/<int:pk>', views.movie_detail, name='movie_detail'),
    path('movies/new', views.movie_create, name='movie_create'),
    path('movies/<int:pk>/edit', views.movie_edit, name='movie_edit'),
    path('movies/<int:pk>/delete', views.movie_delete, name='movie_delete'),
    path('directors/<int:pk>', views.director_detail, name='director_detail'),
    path('directors/', views.director_list, name='director_list'),
    path('directors/new', views.director_create, name='director_create'),
    path('directors/<int:pk>/edit', views.director_edit, name='director_edit'),
    path('directors/<int:pk>/delete', views.director_delete, name='director_delete'),    
    path('movies/<int:pk>/edit', views.movie_edit, name='movie_edit'),
]