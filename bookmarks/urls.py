# from django.conf.urls import url
# from bookmarks import views
# # urlpatterns = [
# #   path('', views.index, name='index'),
# # ]
# app_name = 'bookmarks'

# urlpatterns = [
#     url(r'^$', views.bookmark_list, name='bookmark_list'),
#     url(r'^new$', views.bookmark_create, name='bookmark_new'),
#     url(r'^edit/(?P<pk>\d+)$', views.bookmark_update, name='bookmark_edit'),
#     url(r'^delete/(?P<pk>\d+)$', views.bookmark_delete, name='bookmark_delete'),
# ]

from django.urls import include, re_path
from bookmarks import views
# urlpatterns = [
#   path('', views.index, name='index'),
# ]
app_name = 'bookmarks'

urlpatterns = [
    re_path(r'^$', views.bookmark_list, name='bookmark_list'),
    re_path(r'^new$', views.bookmark_create, name='bookmark_new'),
    re_path(r'^edit/(?P<pk>\d+)$', views.bookmark_update, name='bookmark_edit'),
    re_path(r'^delete/(?P<pk>\d+)$', views.bookmark_delete, name='bookmark_delete'),
]
