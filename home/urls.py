from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


# admin customizations
admin.site.site_header = "WordCounter admin pannel"
admin.site.site_title = "welcome to WordCounter admin pannel"

urlpatterns = [
    path("", views.index, name="index"),
    path("count", views.counter, name="counter"),
    path("signup", views.register, name='signup'),
    path('login', views.login, name='login' ),
    path('logout', views.logout, name='logout'),
    path('history', views.history, name='history'),


    # path('password_reset', views.password_reset, name='password_reset'),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='password/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'), 

    path('admin-panel', views.admin, name='admin'),
    path('delete', views.delete, name='delete'),
    path('add', views.add, name='add'),
    path('deleteUser', views.deleteUser, name='deleteUser'),

]