from django.urls import path
from blogapp import views

urlpatterns=[
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('blogs/', views.blogs,name='blogs'),
    path('blog/create', views.createBlog,name='create_blog'),
    path('user/blog/<int:id>', views.retrive_delete_update_blog,name='retrive_delete_update_blog'),
    path('', views.HomeView.as_view(), name='home'),
]