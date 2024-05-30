from django.contrib import admin
from app.views import User, Permission
from django.contrib.contenttypes.models import ContentType

# Register your models here.
admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Permission)
admin.site.register(ContentType)