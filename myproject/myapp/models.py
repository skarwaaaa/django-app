from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)
  title = models.CharField('タイトル', max_length=50)
  content = models.TextField('内容', max_length=1000)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.title

class Like(models.Model):
  post = models.ForeignKey(Post, verbose_name="投稿", on_delete=models.PROTECT)
  user = models.ForeignKey(User, verbose_name="Likeしたユーザー", on_delete=models.PROTECT)