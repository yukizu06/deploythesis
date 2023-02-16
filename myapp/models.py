from django.db import models
from django.contrib.auth.models import User

class Picture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='images\medicaldata')
    uploaded_at = models.DateTimeField(auto_now_add=True)