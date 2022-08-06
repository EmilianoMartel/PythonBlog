from django.urls import path
from products.views import list_products, list_content, new_content, list_review


urlpatterns = [
    path('list-products/', list_products, name='list_products'),
    path('list-content/', list_content, name='list_content'),
    path('list-review/', list_review, name='list_review'),
    path('list-content/', list_content, name='list_content'),
]