from django.shortcuts import render

from users.models import Users
from users.forms import UsersForm


def home(request):
    return render(request, 'index.html', {})


def list(request):
    all_users = Users.objects.all()
    return render(request, 'list.html', {'all_users': all_users})


def add(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
    form = UsersForm()
    return render(request, 'add.html', {'form': form})