from django.db import models

class Category(models.Model):
    name = models.CharField(null=False ,max_length=50)
    orderlv = models.SmallIntegerField(unique=True, null=False)
    use_tf = models.BooleanField(default=True)
    post_num = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ['orderlv']
        db_table = "category_category"

    def __str__(self):
        return self.name