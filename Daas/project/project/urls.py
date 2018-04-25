"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.views.generic.base import TemplateView
from django.conf.urls import url
from backend.views import grade,count,city,industry,companySize,stage,month,cityneed,comsize,stageneed,user

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^get_Grade$', grade.getGrade, name='get_Grade'),
    url(r'^get_SGrade$', grade.getSGrade, name='get_SGrade'),
    url(r'^get_Count$', count.getCount, name='get_Count'),
    url(r'^get_City$', city.getCity, name='get_City'),
    url(r'^get_Industry', industry.getIndustry, name='get_Industry'),
    url(r'^get_ComSize', companySize.getComSize, name='get_ComSize'),
    url(r'^get_Stage', stage.getStage, name='get_Stage'),
    url(r'^get_Month', month.getMonth, name='get_Month'),
    url(r'^get_CityNeed', cityneed.getCityNeed, name='get_CityNeed'),
    url(r'^get_ComNeed', comsize.getComSizeNeed, name='get_ComNeed'),
    url(r'^get_Sneed', stageneed.getstageNeed, name='get_Sneed'),
    url(r'^get_PJob', count.getPJob, name='get_PJob'),
    url(r'^get_PCom', count.getPCom, name='get_PCom'),
    url(r'^get_PCity', count.getPCity, name='get_PCity'),
    url(r'^get_CList', count.getCList, name='get_CList'),
    url(r'^get_IList', count.getIList, name='get_IList'),
    url(r'^login', user.login, name = 'login'),
    url(r'^regist', user.regist, name = 'regist'),
    url(r'^logout', user.logout, name = 'logout'),
    url(r'^index', user.index, name = 'index'),
    
]
