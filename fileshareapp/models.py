from django.db import models

# Create your models here.
class MyModel(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to="upload/")
    secret_key=models.CharField(max_length=4)
    date_time=models.CharField(max_length=10)

    def __str__(self):
        return self.date_time
    