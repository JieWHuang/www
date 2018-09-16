from django.db import models
from mdeditor.fields import MDTextField
from django.utils import timezone
import time
# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name='文章类别', max_length=20)

    class Meta:
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name='文章标签', max_length=20)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    description = models.CharField(verbose_name='简介', max_length=500, default="简介为空")
    content = MDTextField()
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    modify_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    click_nums = models.IntegerField(verbose_name='点击量', default=0)
    category = models.ForeignKey(Category, verbose_name='文章类别')
    tag = models.ManyToManyField(Tag, verbose_name='文章标签')

    class Meta:
        verbose_name = '我的博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    nickname = models.CharField(verbose_name='昵称', max_length=100)
    email = models.CharField(verbose_name='电子邮件', max_length=100)
    cmt_content = models.TextField(verbose_name='评论内容')
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    blog = models.ForeignKey(Blog, verbose_name='评论文章')

    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cmt_content
