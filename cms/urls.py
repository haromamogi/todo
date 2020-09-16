from django.urls import path
from cms import views
from django.contrib import admin


app_name = 'cms'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),

    path('todo/', views.todo_list, name='todo_list'),
    path('todo/done/', views.todo_list_done, name='todo_list_done'),
    path('todo/todo_done/', views.todo_list_todo_done, name='todo_list_todo_done'),
    path('todo/add', views.todo_edit, name='todo_add'),
    path('todo/mod/<int:todo_id>/', views.todo_edit, name='todo_mod'),
    path('todo/del/<int:todo_id>/', views.todo_del, name='todo_del'),
    path('todo/cpt/<int:todo_id>/', views.todo_complete, name="todo"),

    path('todo/back/<int:todo_id>/', views.todo_back, name="todo_back"),
    path('todo/detail/<int:todo_id>/', views.todo_detail, name="todo_detail"),
]
