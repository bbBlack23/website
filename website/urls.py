from django.contrib import admin
from django.urls import path,include


admin.site.site_header = "Website Admin"
admin.site.site_title = "Website Admin Portal"
admin.site.index_title = "Welcome to Website Researcher Portal"

urlpatterns = [
    path('',include('home.urls')),
    path('admin/', admin.site.urls),
    path('users/',include('userapp.urls')),
]
