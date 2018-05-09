from django.urls import path 

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('bookmarks/create/', views.BookmarkCreate.as_view(), name='bookmark_create'),
  path('bookmarks/<int:pk>/update/', views.BookmarkUpdate.as_view(), name='bookmark_update'),
  path('bookmarks/<int:pk>/delete/', views.BookmarkDelete.as_view(), name='bookmark_delete'),
]