"""
URL configuration for my_wish project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from wish_content.admin import blog_admin_site  # BlogAdminSite import
#chatGPT가 알려준거
# from django.contrib.auth.decorators import login_required
# from django.views.generic import TemplateView

urlpatterns = [
    path('admin/blog/', blog_admin_site.urls),
    path('accounts/', include('allauth.urls')),
    # 사용자 프로필 URL 추가chatGPT가 알려준거
    # path('accounts/profile/', login_required(TemplateView.as_view(template_name='profile.html')), name='user_profile'),///
    path('markdownx/', include('markdownx.urls')),
    path('admin/', admin.site.urls),
    path('', include('wish_content.urls') )
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)