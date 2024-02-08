"""Visuals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path, re_path
from app_management.views import home_view,login_view,get_store_data,MapDataView,get_store_data_store_level,visuals_view  # Import your home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app_management.urls')),
    
    path('', login_view, name='login'),
    path('visuals/', visuals_view, name='visuals'),
    path('Home_Reporting/', home_view, name='home'),  # Add this line to handle the root path
    path('get_store_data/', get_store_data, name='get_store_data'),
    path('get_store_data_store_level/', get_store_data_store_level, name='get_store_data_store_level'),
    path('get_map_data/', MapDataView.as_view(), name='get_map_data'),
]
