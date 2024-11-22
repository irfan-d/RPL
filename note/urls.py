from django.urls import path
from . import views
from django.urls.resolvers import URLPattern

urlpatterns = [
  path('', views.index, name='note.index'),
  path('add/', views.add, name='note.add'),
  path('save/', views.save, name='note.save'),
  path('edit/<int:notes_id>/', views.edit, name='note.edit'),
  path('update/<int:notes_id>/', views.update, name='note.update'),
  path('delete/<int:notes_id>/', views.delete, name='note.delete'),
  # path('update/<int:note_id>/', views.update, name='note.update'),
  # path('delete/<int:note_id>/', views.delete, name='note.delete'),
]
