from .views import RegisterAPI, LoginAPI, UserAPI, UserDataAPI, UserDataAPIDetail
from knox import views as knox_views
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),   
    path('api/useruid/', UserAPI.as_view(), name='useruid'),
    path('api/userdata/', UserDataAPI.as_view(), name='userdata'),
    path('api/userdata/<str:uid>', UserDataAPIDetail.as_view(), name='userdatadetail'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]