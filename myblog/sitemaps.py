from django.contrib.sitemaps import Sitemap

from post.models import Post


class PostSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5
    def items(self):
        return Post.objects.filter(ins_dt__isnull=False).order_by('ins_dt')
    def lastmod(self, obj):
        return obj.upd_dt