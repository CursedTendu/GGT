from django.urls import path
from .views import product_list, product_detail, user_profile, ProductCreateEditDelete, favorite_products,  toggle_favorite

app_name = 'market'

urlpatterns = [
    path('', product_list, name = 'product_list'),
    #path('product/create/', create_product, name='create_product'),
    #path('product/edit/<int:product_id>/', edit_product, name='edit_product'),
    #path('products/delete/<int:product_id>/', delete_product, name='delete_product'),
    path('profile/', user_profile.as_view(), name = 'user_profile'),
    path('product/<int:product_id>/', product_detail, name = 'product_detail'),
    path('favorites/', favorite_products, name = 'favorite_products'),
    path('products/<int:product_id>/toggle_favorite/', toggle_favorite, name = 'toggle_favorite'),
    path('product/create/', ProductCreateEditDelete.as_view(), name = 'create_product'),
    path('product/edit/<int:product_id>/', ProductCreateEditDelete.as_view(), name = 'edit_product'),
    path('product/delete/<int:product_id>/', ProductCreateEditDelete.as_view(), name = 'delete_product'),
]