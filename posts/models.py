from django.db import models

class Post(models.Model):
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='I need help!')
    description = models.TextField()
    loc_lat = models.DecimalField(max_digits=9, decimal_places=6, default=0) 
    loc_long = models.DecimalField(max_digits=9, decimal_places=6, default=0) 
    reward = models.CharField(max_length=100, blank=False, default='I will buy you a coffee.')

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
