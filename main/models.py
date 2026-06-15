from django.db import models

# Create your models here.
class HelloWorldModel(models.Model):
    image = models.FileField(verbose_name="Rasm", upload_to="hello-world-images/")
    title = models.CharField(verbose_name="Sarlavha", max_length=255)