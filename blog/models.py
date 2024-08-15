from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



# users
class Users(AbstractUser):
    full_name= models.CharField(max_length=50,blank=True)
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField(('email'), unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)



    def __str__(self):
        return self.username
    

    #category

class Category(models.Model):
    title = models.CharField(max_length=30)

    # class Meta:
    #     title = "categories"

    def __str__(self):
        return self.title



# post
class Post(models.Model):

    STATUS_CHOICES = (('draft', 'Draft'),('published', 'Published'),)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True) 
    author = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_post')
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,default='draft')

        
    class Meta:
        ordering = ('-published_date',)

    def __str__(self):
        return self.title
    
    
    #comment
class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    
            # or 

    # def __str__(self):
    #     return f"{self.author} on '{self.post}'"

    

