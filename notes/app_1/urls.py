from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoteList.as_view()),
    path('notes/',views.getNotes,name="notes"),
    path('notes/create/',views.createNote,name="create"),
    path('notes/<str:pk>/update/',views.updateNote,name="update"),
    path('notes/<str:pk>/delete/',views.deleteNote,name="delete"),
    path('notes/<str:pk>/',views.getNote,name="note"),

   


]