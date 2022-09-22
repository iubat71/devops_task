from django.urls import path
from . import views 
urlpatterns = [
   
    path('',views.home,name="home"),
    path('product',views.product_refill,name="product"),
    path('update<int:pk>',views.update_view,name="update"),
    path('pupdate<int:pk>',views.pupdate_view,name="pupdate"),
    path('load_package',views.load_package,name="load_package"),
    path('load_product',views.load_product,name="load_product"),
    path('package',views.package,name="package"),
    path('porduct_refill',views.p_refill,name="prefill"),
    path('card',views.card,name="card"),



]
