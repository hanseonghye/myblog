from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(null=False, max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, db_column='parent')
    orderlv = models.SmallIntegerField(null=True)
    use_tf = models.BooleanField(default=True)

    class Meta:
        db_table = "category_category"

    def get_num_children(self):
        return self.get_children().count()

    # def count_post(self):
    #     return self.

    def __str__(self):
        return self.name