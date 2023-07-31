from django.urls import path
from .views import product_list, product_detail, user_profile, ProductCreateEditDelete, favorite_products,  toggle_favorite, profile

app_name = 'market'

urlpatterns = [
    path('', product_list, name = 'product_list'),
    path('user_profile/', user_profile.as_view(), name = 'user_profile'),
    path('profile/<str:username>', profile, name='profile'),
    path('product/<int:product_id>/', product_detail, name = 'product_detail'),
    path('favorites/', favorite_products, name = 'favorite_products'),
    path('products/<int:product_id>/toggle_favorite/', toggle_favorite, name = 'toggle_favorite'),
    path('product/create/', ProductCreateEditDelete.create_product, name = 'create_product'),
    path('product/edit/<int:product_id>/', ProductCreateEditDelete.edit_product, name = 'edit_product'),
    path('product/delete/<int:product_id>/', ProductCreateEditDelete.delete_product, name = 'delete_product'),
]