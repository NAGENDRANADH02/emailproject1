"""
URL configuration for email_builder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include  # Include app URLs
from builder import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('getEmailLayout/', views.get_email_layout, name='get_email_layout'),
    path('uploadImage/', views.upload_image, name='upload_image'),
    path('uploadEmailConfig/', views.upload_email_config, name='upload_email_config'),
    path('renderAndDownloadTemplate/', views.render_and_download_template, name='render_and_download_template'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
