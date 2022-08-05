from django.urls import path
from products.views import list_products, list_content


urlpatterns = [
    path('list-products/', list_products, name='list_products'),
    path('list-content/', list_content, name='list_content'),
]