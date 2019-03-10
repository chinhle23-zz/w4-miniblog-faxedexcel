from django.db import models
from django.urls import reverse
    # Used to generate URLs by reversing the URL patterns
import uuid
    # Required for unique book instances

# Create your models here.

class Blogger(models.Model):
    """Model representing a blogger."""
    username = models.CharField(max_length=100)

    bio = models.TextField(max_length=1000, help_text='Enter a brief bio for the blogger')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.username

    def get_absolute_url(self):
        """Returns the url to access a detail record for this blogger."""
        return reverse('blogger-detail', args=[str(self.id)])

class Blog(models.Model):
    """Model representing a blog post."""
    title = models.CharField(max_length=200, help_text='Enter a title for the blog post')

    post_date = models.DateField()
        # no arguments are passeds since we want the default display "Post date" and we require this field to be filled out

    author = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True) 
        # Foreign Key used b/c blog can only have 1 author, but author can have many blogs
        # 'Blogger' model class argument is declared to connect the relationship between the 'Blog' and 'Blogger' classes
        # 'on_delete=models.SET_NULL' argument sets the value of the author to Null if the associated author record is deleted
        # 'null=True' argument allows the database to store a 'Null' value if no author is selected
    
    description = models.TextField(max_length=2000, help_text='Enter a description for the blog post')

    
    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this blog."""
        return reverse('blog-detail', args=[str(self.id)])
