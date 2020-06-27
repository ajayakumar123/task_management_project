
from django import forms
from django.contrib.auth.models import User
from taskApp.models import Task

class TaskForm(forms.ModelForm):

    assign_to = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple, queryset=User.objects.all(), label='Select User')

    class Meta:
        model = Task
        fields = ('task_name','description','status','assign_to','created_by','created_on')


# class TaskForm2(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ('task_name','description','status','worker','created_by',)