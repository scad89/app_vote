from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vote_page.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('vote_page.urls'))
]

urlpatterns += doc_urls
