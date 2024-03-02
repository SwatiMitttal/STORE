from django.urls import path,include
from . import views

urlpatterns = [
    path('store/<slug:cslug>',views.store,name='prod'),

    path('store/<slug:cslug>/<slug:pslug>',views.pdetail,name='prod-detail'),
    path('store/',views.search,name='search')
]
