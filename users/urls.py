from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('login/',views.ilogin,name='users-login'),
    path('register/',views.iregister,name='users-register'),
    path('',views.index,name='users-index'),
    path('logout/', views.ilogout, name='users-logout'),
    path('forgot/password/', views.forgot_password, name='forgot_password'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'),
             name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'),
             name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'),
             name='password_reset_confirm'),
    path('reset/pasword/<str:token>/', views.reset_password, name='reset_password')
]
















#from . import views
#from django.conf.urls.static import static

#urlpatterns=[
   # path('login/',views.ilogin,name='users-login'),
    #path('register/',views.iregister,name='users-register'),
    #path('',views.index,name='users-index'),
    #path('logout/', views.ilogout, name='users-logout'),
    #path('jobs', views.ilogout, name='users-jobs'),
    #path('activate/<str:token>/', views.activate_user, name='activate'),
    #path('resend/activation/link/', views.resend_activation_link, name='resend_activation_link'),
    #path('forgot/password/', views.forgot_password, name='forgot_password'),
    #path('reset_password/', views.reset_password, name='reset_password')

    
#]
