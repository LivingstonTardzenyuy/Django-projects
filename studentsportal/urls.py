from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('notes',views.notes,name='notes'),
    path('delete_note/<int:pk>',views.delete_note,name='delete_note'),
    path('notes_detail/<int:pk>/',views.NotesDetailView.as_view(),name='note-detail'),
    path('homework',views.homework,name='homework'),
    path('delete_homework/<int:pk>',views.delete_homework,name='delete_homework'),
    path('update_homework/<int:pk>',views.update_homework,name='update_homework'),
    path('youtube',views.youtube,name='youtube'),
    path('todo',views.todo,name='todo'),
    path('delete_todo/<int:pk>',views.delete_todo,name='delete_todo'),
    path('update_todo/<int:pk>',views.update_todo,name='update_todo'),
    path('books',views.books,name='books'),
    path('dictionary',views.dictionary,name='dictionary'),
    path('wiki',views.wiki,name='wiki'),
    path('conversion',views.conversion,name='conversion'),
    path('note_detail/<int:pk>',views.note_detail,name='note_detail'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('profile',views.profile,name='profile'),

    path('chat', views.chat, name='chat'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview')
]