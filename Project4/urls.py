from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from viewscrud.views import *

router = DefaultRouter()

router.register('empapi', EmpViewSet, basename = 'emp' )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path("", include(router.urls)),
]
