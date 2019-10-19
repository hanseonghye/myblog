from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from taggit.managers import TaggableManager

from category.models import Category


class Post(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    content = MarkdownxField()
    ins_dt = models.DateTimeField(auto_now_add=True)
    upd_dt = models.DateTimeField(auto_now=True)
    use_tf = models.BooleanField(default=True)
    tags = TaggableManager()


    class Meta:
        ordering = ['-ins_dt']

    @property
    def formatted_markdown(self):
        return markdownify(self.content)


    @property
    def get_tag(self):
        return self.tags.most_common()







