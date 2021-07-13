from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    born_date = models.DateField()

    class Meta:
        db_table = 'tb_authors'
class Book(models.Model):
    hauthor = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_date = models.DateField()
    country = models.CharField(max_length=20)
    # 在第三条的d 个人感觉需要加一个字段 才能根据书名去查询信息
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'tb_books'

