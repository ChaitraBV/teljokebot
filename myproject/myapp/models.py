from django.db import models

# Create your models here.
#from django.db import models
from django.contrib.auth.models import User

class ButtonCalls(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    button_name = models.CharField(max_length=50)
    call_count = models.PositiveIntegerField(default=0)

