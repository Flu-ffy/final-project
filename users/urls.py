from django.urls import path,include
from . import views
from django.conf.urls.static import static

urlpatterns=[
    path('login/',views.ilogin,name='users-login'),
    path('register/',views.iregister,name='users-register'),
    path('index/',views.index,name='users-index'),
    path('logout/', views.logout, name='users-logout'),
    path('password-reset/', views.PasswordReset,name = 'users-reset_password'),
    path('password-reset/done/', views.PasswordResetDone,name = 'users-password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',  views.PasswordResetConfirm,name = 'users-password_reset_confirm'),
    path('password-reset-complete/', views.PasswordResetComplete,name = 'users-password_reset_complete'),
    
    path('', include('users.urls')),

]
