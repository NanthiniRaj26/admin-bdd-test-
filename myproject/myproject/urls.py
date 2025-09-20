from django.contrib import admin
from django.urls import path
from core.views import ReportView, home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('report/', ReportView.as_view(), name='report'),
]