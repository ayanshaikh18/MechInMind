from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from django.views.generic import TemplateView

from . import settings
from Article.views import list

urlpatterns = [
    path('', list),
    path('admin/', admin.site.urls),
    url(r'^markdownx/', include('markdownx.urls')),
    path('articles/', include('Article.urls')),
    path('chunkConcept/', TemplateView.as_view(template_name="chunkConcept.html")),
    path('meetTheTeam/', TemplateView.as_view(template_name="meet the team.html"))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)