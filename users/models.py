from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, Permission


class User(AbstractUser):
    
    role = models.CharField(max_length=50, choices=[('Admin', 'Admin'), ('Member', 'Member')], default='Member')

   
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    

    def __str__(self):
        return self.user.username
