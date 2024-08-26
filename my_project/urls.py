from django.contrib import admin
# from django.urls import path
from django.urls import path, include
# from mysite import views

urlpatterns = [
    # path('mysite/', views.index),
    path('admin/', admin.site.urls),
    path('mysite/', include('mysite.urls')),
    path('', include('pages.urls')),
]
