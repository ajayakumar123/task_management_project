from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
import datetime
#Create your models here.
# from django.contrib.auth.models import AbstractUser
#
#
# class User(AbstractUser):
#
#     ROLE_CHOICES=(('lead','Lead'),('worker','Worker'))
#     user_role = models.CharField(max_length=30,choices=ROLE_CHOICES,default='worker')
#
#     def __str__(self):
#         return str(self.username)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES=(('lead','Lead'),('worker','Worker'))
    user_role = models.CharField(max_length=30,choices=ROLE_CHOICES,default='worker')

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Task(models.Model):
    task_name=models.CharField(max_length=30)
    description = models.TextField()
    status_choice = (('not_started', 'Not started'), ('inprogress', 'Inprogress'), ('done', 'Done'))
    status = models.CharField(max_length=30, choices=status_choice, default="not_started")
    worker = models.ForeignKey(User,related_name='tasks', related_query_name='task', null=True,blank=True)
    assign_to = models.ManyToManyField(User,related_name='tasks_many', related_query_name='q_task',blank=True)
    created_by = models.CharField(max_length=50, blank=True)
    created_on = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now)

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reverse('task_list')

    def get_assign_to(self):
        return "\n".join([p.username for p in User.objects.all()])