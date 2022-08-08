from django.urls import path
from products.views import list_products, list_content, new_content, list_review, search_content
from products import views


urlpatterns = [
    path('list_products/', list_products, name='list_products'),
    path('list_content/', list_content, name='list_content'),
    path('listeview/', list_review, name='list_review'),
    path('new_content/', new_content, name='new_content'),
    path('search_content/', search_content, name='search_content'),
    ]