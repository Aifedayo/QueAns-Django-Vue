"""QueAns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from core.views import IndexTemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django_registration.backends.one_step.views import RegistrationView
from users.forms import CustomUserForm

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/register/',
        RegistrationView.as_view(form_class=CustomUserForm, success_url='/'),
        name='django_registration_register'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('api-auth/', include('rest_framework.urls')),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('api/v1/', include('questions.api.urls')),

    re_path(r"^(?!media).*$", IndexTemplateView.as_view(), name="spa-entry-point")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                                document_root=settings.MEDIA_ROOT)
