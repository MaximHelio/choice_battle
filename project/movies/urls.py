from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]