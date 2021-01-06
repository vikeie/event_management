from django.urls import path 
from . import views 

urlpatterns = [ 
    path('register/', views.RegisterApiView.as_view(), name='register_api'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('events/', views.EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),

    path('api/token/', views.CustomTokenObtainPairView.as_view(), name ='token_obtain_pair'), 
]
