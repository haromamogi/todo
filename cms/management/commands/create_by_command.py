from django.core.management.base import BaseCommand

from cms.models import Todo

from cms.forms import TodoForm
from cms.views import *


def create():
    print('content')
    content = input()
    print('limit')

    limit = input()

    #data = [content, limit]
    todo = Todo(duty=content, limit=limit)
    todo.save()
    return


def todo_list_by_co():
    todos = Todo.objects.all().order_by('id')

    for todo in todos:
        print(todo.id, todo)


def todo_delete_by_co():
    todos = Todo.objects.all().order_by('id')

    for todo in todos:
        print(todo.id, todo)

    print("the key number or Name")
    key = input()
    if key.isdigit():
        print(key)
        todo_id = int(key)

        todo = Todo.objects.get(pk=todo_id)
        todo.delete()
        return True

    else:
        todo = Todo.objects.get(duty=key)
        if todo:
            todo.delete()
            return True
        else:
            print("err")
            return False


class Command(BaseCommand):
    help = 'Display the number of blog articles'

    def add_arguments(self, parser):
        parser.add_argument('todo_option', nargs='+', type=int)

    def handle(self, *args, **options):
        print(args)
        print(options)
        print(options['todo_option'])
        if options['todo_option'] == [1]:
            create()
            self.stdout.write(self.style.SUCCESS('ToDo Successfully Complete'))
        elif options['todo_option'] == [2]:
            todo_list_by_co()
        elif options['todo_option'] == [3]:
            if todo_delete_by_co():
                self.stdout.write(self.style.SUCCESS('消去しました'))
            else:
                self.stdout.write(self.style.SUCCESS('消去できませんでした'))

