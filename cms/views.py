from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from cms.models import Todo
from cms.forms import TodoForm
from itertools import zip_longest


def index(request):
    return render(request, 'cms/top.html')


def profile(request):
    return render(request, 'cms/profile.html')


def todo_list(request):
    todos = Todo.objects.filter(existence=True).order_by('id')
    return render(request,
                  'cms/todo_list.html',
                  {'todos': todos})


def todo_list_done(request):
    todos = Todo.objects.filter(existence=False).order_by('id')
    return render(request,
                  'cms/todo_list_d.html',
                  {'todos': todos})


def todo_list_todo_done(request):
    todos_true = Todo.objects.filter(existence=True).order_by('id')
    todos_false = Todo.objects.filter(existence=False).order_by('id')
    #max_count = todos_true.count() if todos_true.count() > todos_false.count() else todos_false.count()
    # table = [todos_true, todos_false]
    # print(table)


    table = zip_longest(todos_true, todos_false)

    return render(request,
                  'cms/todo_list_t_d.html',
                  {'true': todos_true, 'false': todos_false, 'table': table, })


def todo_edit(request, todo_id=None):

    if todo_id:
        todo = get_object_or_404(Todo, pk=todo_id)
    else:
        todo = Todo()

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('cms:todo_list')
    else:
        form = TodoForm(instance=todo)

    return render(request, 'cms/todo_edit.html', dict(form=form, todo_id=todo_id))


def todo_del(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect('cms:todo_list')


def todo_complete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.existence = False
    todo.save()
    return redirect('cms:todo_list')


def todo_back(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.existence = True
    todo.save()
    return redirect('cms:todo_list')

