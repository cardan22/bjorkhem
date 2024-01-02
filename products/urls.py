from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail.as_view(), name='product_detail'),
    path('favorites/', views.favorite_products.as_view(), name='favorite_products'),
    path(
        'add-favorite-product/<int:product_id>/', views.add_favorite_product.as_view(),
        name="add_favorite_product"),
    path('add/', views.add_product, name='add_product'),    
]