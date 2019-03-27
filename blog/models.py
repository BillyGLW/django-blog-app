from django.contrib.auth import get_user_model

from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser,
	BaseUserManager,
	)

from ckeditor.fields import RichTextField

class BlogPost(models.Model):
    author = models.ForeignKey("blog.MyUser",on_delete = models.CASCADE,verbose_name = "Smith")
    title = models.CharField(max_length = 50,verbose_name = "Lorem ipsum")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Dorem sit")
    article_image = models.FileField(blank = True,null = True,verbose_name="Amet")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']

class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost,on_delete = models.CASCADE,verbose_name = "post",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "John")
    comment_content = models.CharField(max_length = 200,verbose_name = "Fancy content")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']


class MyUserManager(BaseUserManager):

    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(default="1995-01-16")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'

    def get_full_name(self):
    	return self.email
    def get_short_name(self):
    	return self.email
    def __unicode__(self):
    	return self.email
    	
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
	

class BlogCPosts(models.Model):
    post = models.TextField(max_length=999)
    post_title = models.CharField(max_length=20)
    post_description = models.TextField(max_length=999)
    ppost_date = models.DateTimeField('date published')

class MusicAlbum(models.Model):
    title = models.TextField(max_length=24)
    description = models.TextField(max_length=127)

MyUser = get_user_model()
