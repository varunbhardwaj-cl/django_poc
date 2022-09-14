from django.urls import path
from .views import *


urlpatterns = [
    path('cb/', CustomerList.as_view(), name='class_base_index'),
    path('fb/', get_users, name='function_base_index'),
    path('cb/<int:pk>/', CustomerDetail.as_view(), name='class_base_detail'),
    path('fb/<int:pk>/', get_user, name='function_base_detail'),
    path('cb/create/', CustomerCreate.as_view(), name='class_base_create'),
    path('cb/update/<pk>/', CustomerUpdate.as_view(), name='class_base_update'),
    path('cb/delete/<pk>/', CustomerDelete.as_view(), name='class_base_delete'),
    path('fb/create/', create_user, name='function_base_create'),
    path('fb/update/<pk>/', update_user, name='function_base_update'),
    # index page
]