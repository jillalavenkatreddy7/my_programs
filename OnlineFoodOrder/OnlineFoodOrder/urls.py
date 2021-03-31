"""OnlineFoodOrder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from OnlineFood import views
from OnlineFoodOrder import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name='index'),
    path('Entry/',views.entry,name="entry"),
    path('Validate/',views.validate,name='send'),
    path('addFood/',views.addFodd,name="addfood"),
    path('logout/',views.logout,name="logout"),
    path('logout1/',views.logout1,name="logout1"),
    path('previous/',views.previous,name="back"),
    path('save/',views.saveFood,name="save"),
    path('ViewFoods/',views.viewFoods,name="viewfoods"),
    path('delete/',views.deleteFood,name="delete"),
    path('update/',views.updateFood,name="update"),
    path('updatedata',views.updatedataFood,name="updatedata"),
    path('Back/',views.back,name="back1"),
    path('newcustomer/',views.newcustomer,name='newcustomer'),
    path('backcustomer/',views.backcustomer,name='backcustomer'),
    path('newcustomersave/',views.newcustomersave,name='newcustomersave'),
    path('customerlogin/',views.customerlogin,name='customerlogin'),
    path('customerViewFoods/',views.customerViewFoods,name='customerViewFoods'),
    path('backcustomer1/',views.backcustomer1,name='backcustomer1'),
    path('order/',views.order,name='order'),
    path('ordersave/',views.ordersave,name='ordersave')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)