from django.urls import path 
from . import views 

urlpatterns = [ 
    path('hello/', views.HelloView.as_view(), name ='hello'),
    # path('register/', views.RegisterApiView.as_view(), name='register_api'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail')
]
