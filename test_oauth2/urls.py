"""
URL configuration for test_oauth2 project.

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
from django.urls import path, include
from app.views import UserRUD, UserList, UserCreate, GroupLC, GroupRUD, PermissionsLC, CheckPermission, ContentTypeLC

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('contenttypes/', ContentTypeLC.as_view()),
    path('permissions/', PermissionsLC.as_view()),
    path('groups/', GroupLC.as_view()),
    path('groups/<pk>', GroupRUD.as_view()),
    path('user_list/', UserList.as_view()),
    path('user_create/', UserCreate.as_view()),
    path('users/<username>', UserRUD.as_view()),
    path('check_permission/', CheckPermission.as_view())
]
