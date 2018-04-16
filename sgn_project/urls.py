from django.contrib import admin
from django.urls import path, include
from sgn_project import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.login_redirect, name='login_redirect'),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('home/', include('home.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
