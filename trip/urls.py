"""trip URL Configuration

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
from guide import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.display),
    path('sec',views.add),
    path('login',views.log, name="login"),
    path('out',views.logout),
    path('serv',views.service),
    path('gall',views.gallery),
    path('cont',views.contact),
    path('abo',views.about),
    path('des',views.destination),
    path('him',views.himalayan),
    path('hre',views.resort),
    path('boo',views.book),
    path('ga',views.go),
    path('ag',views.aagran),
    path('ma',views.maha),
    path('oo',views.oot),
    path('hy',views.hydh),
    path('ass',views.aass),
    path('ba',views.bangalu),
    path('gre',views.resogoa),
    path('agr',views.resoagra),
    path('mare',views.resomaha),
    path('oore',views.resoot),
    path('hyr',views.resohy),
    path('asr',views.resoass),
    path('bare',views.resoban),
    path('reso',views.room),
    path('bu',views.bus),
    path('bbu',views.bbook),
    path('card-payment/<int:amount>', views.card_payment),
    path('process_payment', views.process_payment),
    path('book_room/<str:room_type>', views.book_room),
    path('r_booking/<str:room_type>', views.r_booking),
    
    
]
