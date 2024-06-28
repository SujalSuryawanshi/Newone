from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Flaky import settings
urlpatterns = [
    path("", include('core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_URL)
urlpatterns += staticfiles_urlpatterns()