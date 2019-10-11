from django.urls import path 
from . import views

urlpatterns = [
    path('', views.NoteList.as_view(), name='note_list'),
    path("<int:pk>/", views.NoteDetail.as_view(), name="note_detail")
]
