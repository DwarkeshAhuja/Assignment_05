"""Assignment_05 URL Configuration

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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from Assignment_05.home import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home Page URL
    path('', views.home, name='home'),

    # HeatMap Page URL
    #path('heatmap/', views.heatmap, name='heatmap'),

    # Linegraph Page URL
    #path('linegraph/', views.linegraph, name='linegraph'),

    # Code Page URL
    #path('code/', views.code, name='code')
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)