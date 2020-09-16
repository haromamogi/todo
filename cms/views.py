from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect

from cms.models import Todo
from cms.forms import TodoForm
from itertools import zip_longest


def index(request):
    return render(request, 'cms/top.html')


def profile(request):
    return render(request, 'cms/profile.html')


def paginate_queryset(request, queryset, count):
    """Pageオブジェクトを返す。

    ページングしたい場合に利用してください。

    countは、1ページに表示する件数です。
    返却するPgaeオブジェクトは、以下のような感じで使えます。

        {% if page_obj.has_previous %}
          <a href="?page={{ page_obj.previous_page_number }}">Prev</a>
        {% endif %}

    また、page_obj.object_list で、count件数分の絞り込まれたquerysetが取得できます。

    """
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


def todo_list(request):
    todos = Todo.objects.filter(existence=True).order_by('id')
    page_obj = paginate_queryset(request, todos, 10)
    context = {
        'todos': page_obj.object_list,
        'page_obj': page_obj,
    }
    return render(request,
                  'cms/todo_list.html',
                  context)


def todo_list_done(request):
    todos = Todo.objects.filter(existence=False).order_by('id')
    page_obj = paginate_queryset(request, todos, 10)
    context = {
        'todos': page_obj.object_list,
        'page_obj': page_obj,
    }
    return render(request,
                  'cms/todo_list_d.html',
                  context)


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

