from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView,UpdateView
from .models import Task

from django.contrib import messages


class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'

class Taskdetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'
class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('SL_No','Item_Name','Description')
    def get_success_url(self):
        return reverse_lazy('cbvdetails', kwargs={'pk': self.object.id})

class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

def doc(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        SL_No = request.POST.get('Serial', '')
        Item_Name = request.POST.get('Item_Name', '')
        Description = request.POST.get('Description', '')
        task = Task(SL_No=SL_No, Item_Name=Item_Name, Description=Description)
        task.save()
        messages.success(request, 'Data created successfully.')
    return render(request, 'home.html',{'task1':task1})

def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')



def update(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.SL_No = request.POST.get('SL_No', '')
        task.Item_Name = request.POST.get('Item_Name', '')
        task.Description = request.POST.get('Description', '')
        task.save()
        return redirect('/')
    return render(request, 'edit.html', {'task': task})




   


