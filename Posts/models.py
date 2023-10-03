from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
'''
    - title  done
    - author
    - content  done
    - image  done
    - publish_date  done
    - tags done
'''
'''
    - fields
    - html widget
    - validation
'''
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length= 50000)
    publish_date = models.DateTimeField()
    tags = TaggableManager()
    image = models.ImageField(upload_to='postimages')

    def __str__(self):
        return self.title