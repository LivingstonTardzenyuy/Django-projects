from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class PostModel(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)
    
    
    #to handle comments count
    def comment_count(self):
        return self.comment_set.all().count()
    
    def comments(self):
        return self.comment_set.all()
    
    # comment_set.all reversed
    
    def __str__(self):
        return self.author.username
    
    class Meta:
        verbose_name = 'PostModel'
        verbose_name_plural = 'PostModel'
        
        
    #comment section not the following
    #A User can have many comments that's why we us as a ForeignKey not as a OneToOne
    #a post can have many comments too
class Comment(models.Model):     
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content= models.CharField(max_length=250)
    
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comment"     