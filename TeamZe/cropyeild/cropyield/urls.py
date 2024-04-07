
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='yieldapp/')),
    path('admin/', admin.site.urls),
    path('yieldapp/', include('yieldapp.urls')),
]
