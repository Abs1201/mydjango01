from django.db import models

# Create your models here.
# 데이터 저장의 형태를 설정


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
