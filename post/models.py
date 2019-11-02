from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import F
from hitcount.models import HitCountMixin, HitCount
from taggit.managers import TaggableManager
from category.models import Category


class Post(models.Model, HitCountMixin):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    content = RichTextUploadingField()
    ins_dt = models.DateTimeField(auto_now_add=True)
    upd_dt = models.DateTimeField(auto_now=True)
    use_tf = models.BooleanField(default=True)
    tags = TaggableManager(blank=True)
    # hit_count_generic = GenericRelation(
    #     HitCount, object_id_field='id',
    #     related_query_name='hit_count_generic_relation', db_column='hit', default=0)


    class Meta:
        ordering = ['-ins_dt']
        db_table = "post_post"

    def __str__(self):
        return f'Post {self.pk}/{self.title}'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Category.objects.filter(id=self.category_id).update(post_num=F('post_num') + 1)


    @property
    def get_tag(self):
        return self.tags.most_common()







