from django.urls import path
from . import views

app_name = "users_app"

urlpatterns = [
    #template login
    path(
        'login/',
        views.LoginUser.as_view(),
        name='login'
    ),
    path(
        'api/google-login/',
        views.GoogleLoginView.as_view(),
        name='users-google_login'
    )
        
            
]
