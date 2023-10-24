from django.db import models

# Create your models here.
class URLShortener(models.Model):
  long_url=models.URLField()
  short_code=models.CharField(max_length=10,unique=True)
  click_count = models.PositiveIntegerField(default=0)  
  
  def __str__(self):
    return self.long_url
  