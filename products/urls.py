from django.urls import path, include
from products.views import New_platform, Delete_content, Delete_review, Update_content, Update_review, list_content, new_content, list_review, search_content, new_review, list_platforms, Delete_platform


urlpatterns = [
    #path('', index, name='index'), # ///FALTA///
    path('list-content/', list_content, name='list_content'),
    path('list-review/', list_review, name='list_review'),
    path('new-content/', new_content, name='new_content'),
    path('search-content/', search_content, name='search_content'),
    path('new-review/', new_review, name='new_review'),
    path('new-platform/', New_platform.as_view(), name='new_platform'),
    path('list-platforms/', list_platforms, name='list_platforms'),
    path('delete-platform/<int:pk>/', Delete_platform.as_view(), name='delete_platform'),
    path('users/', include('users.urls')),
    path("delete-content/<int:pk>/", Delete_content.as_view(), name="delete_content"),
    path("delete-review/<int:pk>/", Delete_review.as_view(), name="delete_review"),
    path("update-content/<int:pk>/", Update_content.as_view(),name="update_content"),
    path("update-review/<int:pk>/", Update_review.as_view(),name="update_review"),
]