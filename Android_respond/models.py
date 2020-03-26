from django.db import models

# Create your models here.
class class_Android_user(models.Model):
    user_name = models.CharField(max_length=10)
    user_password = models.CharField(max_length=20)
    user_friends = models.TextField()
    user_groups = models.TextField()
    user_message_cache = models.TextField()
    user_IP = models.CharField(max_length=30)
    user_TTL = models.CharField(max_length=30)

    def __str__(self):
        return "<class_Android_user : %s>" % self.user_name
    
class class_Android_group(models.Model):
    group_mate = models.TextField()
    group_name = models.CharField(max_length=20)
    group_message = models.TextField()
    
    def __str__(self):
        return "<class_Android_group : %s>" % self.user_name
