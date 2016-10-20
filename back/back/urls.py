from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api-web/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('ngrest.urls'))
]
