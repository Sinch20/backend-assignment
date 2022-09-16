from django.contrib import admin
from django.urls import path, include 
from base.views import employeeListView, userDetail
from base.views import EmployeeListView
from base.mypagination import MyLimitOffsetPagination
from api import views


urlpatterns = [
    path('api/users', employeeListView),
    path('api/users/<str:pk>', userDetail),
    # path('api/users/<str:pk>', updateEmployee),
    # path('api/users/<str:pk>', deleteEmployee),
    path('api/usersearch', EmployeeListView.as_view())    
]