"""dproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from myapp import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('call',v1.call),
    # path('renderhtml',v1.renderhtml),
    # path('render_1',v1.render_1),
    # path('render_2',v1.render_2),   
    # path('render_4',v1.render_4),
    # path('dict',v1.render_5), 
    path('',v1.renderpage2),
    path('Savedata',v1.Savedata),
    path('searchdata',v1.searchdata),
    path('Viewallrecord',v1.Viewallrecord),
    path('deletedata',v1.deletedata),
    path('updatedata',v1.updatedata),

]
