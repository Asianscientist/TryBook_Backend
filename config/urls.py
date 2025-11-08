
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/library/', include('books.urls')),
    path('api/', include('recommendations.urls')),
    path('api/', include('reading_history.urls'))
]
