from django.urls import path
from . import views

urlpatterns = [
    # Basic pages
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    # User complaint actions
    path('file-complaint/', views.file_complaint, name='file_complaint'),
    path('my-complaint/', views.my_complaint, name='my_complaint'),
    path('edit-complaint/<int:cid>/', views.edit_complaint, name='edit_complaint'),
    path('delete-complaint/<int:cid>/', views.delete_complaint, name='delete_complaint'),

    # Admin
    path('admin-home/', views.admin_home, name='admin_home'),
    path('admin-all-firs/', views.admin_all_firs, name='admin_all_firs'),
    path('update-status/<int:cid>/', views.update_status, name='update_status'),
]
