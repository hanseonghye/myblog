from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from hitcount.models import HitCountMixin, HitCount
from mptt.fields import TreeForeignKey
from taggit.managers import TaggableManager

from category.models import Category


class Post(models.Model, HitCountMixin):
  title = models.CharField(max_length=50)
  desc = models.TextField(default='')
  category = TreeForeignKey(Category, null=True, on_delete=models.SET_NULL)
  content = RichTextUploadingField()
  ins_dt = models.DateTimeField(auto_now_add=True)
  upd_dt = models.DateTimeField(auto_now=True)
  use_tf = models.BooleanField(default=True)
  tags = TaggableManager(blank=True)

  class Meta:
    ordering = ['-ins_dt']
    db_table = "post_post"

  def __str__(self):
    return f'Post {self.pk}/{self.title}'

  def get_absolute_url(self):
    return reverse('post:index', args=[self.pk])

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

  @property
  def get_tag(self):
    return self.tags.most_common()
