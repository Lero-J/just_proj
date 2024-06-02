from django.shortcuts import render, redirect

from myapp.models import Task


# Create your views here.



def index(request):
    tasks = Task.objects.all()
    ctx = {'tasks': tasks}
    return render(request, 'myapp/index.html', context=ctx)



def task_detail(request, task_id):
    task = Task.objects.get(pk=task_id)
    ctx = {'task': task}
    return render(request, 'myapp/task.info.html', context=ctx)


def add_task(request):
    task = Task()
    task.name = request.POST.get('task_name')
    task.description = request.POST.get('task_description')
    task.save()
    return redirect(index)


def mark_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.is_done == True:
        task.is_done = False
    else:
        task.is_done = True
    task.save()
    return redirect(index)

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect(index)




