from django.contrib import admin
from django.urls import path, include

from babka.views import page_not_found, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('babka.urls'))
]

handler404 = page_not_found
