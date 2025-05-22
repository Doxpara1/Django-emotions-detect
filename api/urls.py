from django.urls import path
from .views import UserFormView, UserListView

urlpatterns = [
    path('', UserFormView.as_view(), name='user_form'),
    path('saved/', UserListView.as_view(), name='user_list'),
]