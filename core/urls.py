from django.urls import path

from . import views

urlpatterns = [
    path('', views.categories_list, name='categories_list'),
    path('category/<int:id>/', views.products_list, name='products_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail')
]
