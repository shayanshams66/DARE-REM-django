from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin


urlpatterns = patterns(
    "",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r'^Jobs/$', 'job_management.views.Jobs', name='Jobs'),
    url(r'^dataAnalysis/$','job_management.views.Ibiomes', name='dataAnalysis'),
    url(r'^forms/$','job_management.views.forms', name='forms'),
    url(r'^forms3/$','job_management.views.Files', name='forms3'),
    url(r'^update/$', 'job_management.views.update',name='update'),
    url(r'^ICM/$', 'ICM.views.ICM',name='ICM'),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
