from django.forms import ModelForm
from cms.models import Todo


class TodoForm(ModelForm):

    class Meta:
        model = Todo
        fields = ('duty', 'limit', 'image')
