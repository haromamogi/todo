from django.urls import path
from cms import views


app_name = 'cms'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('todo/', views.todo_list, name='todo_list'),
    path('todo/add', views.todo_edit, name='todo_add'),
    path('todo/mod/<int:todo_id>/', views.todo_edit, name='todo_mod'),
    path('todo/del/<int:todo_id>/', views.todo_del, name='todo_del'),
]

