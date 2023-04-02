from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('postDetails/<int:pk>/', views.postDetails, name="postDetails"),
    path('edit_post<int:pk>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post')

]
