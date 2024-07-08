
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
import notifications.urls
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('notifications/', include(notifications.urls, namespace='notifications')),
    path('signupformpage/',signupformpage , name='signupformpage'),
    path('signinformpage/',signinformpage , name='signinformpage'),
    path('dashboard/',dashboard , name='dashboard'),
    
    path('',include('app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
