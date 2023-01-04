#Import from the core django
from django.db import models
# Import from the third library
from mptt.models import MPTTModel ,TreeForeignKey

class Book(MPTTModel):
    LEFT = 0
    RIGHT = 1
    
    POSITION_CHOICES = (
                     (LEFT, 'left'),
                     (RIGHT, 'right'),
                     )

    title = models.CharField(max_length=300,blank=True)
    description=models.CharField(max_length=300,blank=True)
    position =models.IntegerField(choices=POSITION_CHOICES,null=True,blank=True)
    parent = TreeForeignKey('self',null=True,blank=True,related_name='children' , on_delete=models.CASCADE)

    def __str__(self):
        return self.title