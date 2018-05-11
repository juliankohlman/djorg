"""djorg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# from bookmarks import views
# from django.conf.urls import url

# from django.views.generic import RedirectView, TemplateView
# import bookmarks.views as BookmarkViews
# import generic views TemplateView takes in and returns template * line 18

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', RedirectView.as_view(url='/bookmarks/', permanent=True)),
#     path('bookmarks/', BookmarkViews.bookmarks.as_view()),
#     path('bookmarks/', include('bookmarks.urls')),
# ]
app_name = 'bookmarks'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookmarks.urls', namespace='bookmarks')),
    path('bookmarks/', include('bookmarks.urls', namespace='bookmarks')),
    # url(r'^$', views.bookmark_list, name='bookmark_list'),
    # url(r'^new$', views.bookmark_create, name='bookmark_new'),
    # url(r'^edit/(?P<pk>\d+)$', views.bookmark_update, name='bookmark_edit'),
    # url(r'^delete/(?P<pk>\d+)$', views.bookmark_delete, name='bookmark_delete'),        
]
