from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = models.CharField(null=False, max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, db_column='parent')
    orderlv = models.SmallIntegerField(null=True)
    use_tf = models.BooleanField(default=True)

    class Meta:
        db_table = "category_category"


    def __str__(self):
        return self.name
