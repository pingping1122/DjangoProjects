from django.db import models

# Create your models here.

class Article(models.Model):
    # 文章ID
    article_id=models.AutoField(primary_key=True)
    # 文章标题
    article_title=models.TextField()
    # 文章摘要
    brief_content=models.TextField()
    # 文章内容
    content = models.TextField()
    # 文章发布日期
    publish_date=models.DateTimeField(auto_now=True)

   # 注：函数前后两个下划线
    def __str__(self):
        return self.article_title
