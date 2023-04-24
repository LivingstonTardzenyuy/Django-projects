from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('items', views.items, name= 'items'),
    path('purchase_items<pk>', views.purchase_items, name= 'purchase_items'),
    path('admin_dashboard', views.admin_dashboard, name= 'admin_dashboard'),
    path('delete_product<pk>', views.delete_product, name= 'delete_product'),
    path('add_products', views.add_products, name= 'add_products'),
]