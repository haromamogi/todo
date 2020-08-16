from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from cms.models import Todo
from cms.forms import TodoForm


def index(request):
    return render(request, 'cms/top.html')


def todo_list(request):
    todos = Todo.objects.all().order_by('id')
    return render(request,
                  'cms/todo_list.html',
                  {'todos': todos})


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

