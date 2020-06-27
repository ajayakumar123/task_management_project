from django.shortcuts import render,redirect
from taskApp.forms import TaskForm
from django.contrib.auth.models import User
from taskApp.models import Task
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse


# Create your views here.


def task_list_view(request):
    print("tasks list view")
    user_role = request.user.profile.user_role
    if user_role=='worker':
        task_list=Task.objects.filter(worker=request.user.id)
        print("task_list",task_list)
    else:
        task_list = Task.objects.all()
        print("lead role")
    print("tasks",task_list)
    return render(request, 'task/task_list.html', context={'task_list': task_list,'user_role':user_role})


def user_detail_view(request,id):
    print("user detail view")
    user_data = User.objects.get(id=id)
    print("tasks",user_data)
    print("user name:",user_data.username,user_data.profile.user_role)
    return render(request, 'task/user_data.html', context={'user_data': user_data})


def task_create_view(request):
    print("11111111---task create.....started")
    form=TaskForm()
    if request.method=='POST':
        print("222222--post")
        form = TaskForm(request.POST)
        if form.is_valid():
            task_name = form.cleaned_data['task_name']
            description = form.cleaned_data['description']
            status = form.cleaned_data['status']
            assign_to = form.cleaned_data['assign_to']
            created_on = form.cleaned_data['created_on']
            created_by = form.cleaned_data['created_by']
            task_obj = form.save(commit=True)
            for assign in assign_to:
                task_obj.assign_to.add(assign)
            assign_to_qs=task_obj.assign_to.all()
            print("3333333333",task_obj)

            for user_obj in assign_to_qs:
                print("4444444444")
                Task.objects.create(task_name=task_name, description=description, status=status,
                                    created_on=created_on,created_by=created_by,worker=user_obj)
            task_obj.delete()
            return redirect('/task_list')
    return render(request,'task/task_create.html',{'form':form})


class TaskUpdateView(UpdateView):
    model=Task
    template_name = 'task/task_update1.html'
    fields=('task_name','description','status','worker','created_by')


class TaskDeleteView(DeleteView):
    model=Task
    template_name = 'task/task_delete.html'
    success_url = reverse_lazy('task_list')


def validate_workers_selection(request):
    '''this function will helpful to lead to select only workers for the task.
    if we select lead it will show message that he is also lead'''

    print("1111111111started...",request.GET)

    assign_to=request.GET.get('assign_to')
    use_obj=User.objects.get(id=int(assign_to))
    role=use_obj.profile.user_role
    user_name=use_obj.username
    print("user details",user_name,role)
    if role=='lead':
        user_warn='{0} have a lead role.It is not recommended to assign work for lead role'.format(user_name)

    out_data = {

        'user_warn':user_warn
    }
    return JsonResponse(out_data)


