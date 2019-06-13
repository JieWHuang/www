from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from blog.models import Blog, Category, Tag, Comment
from blog.forms import CommentForm
import markdown
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'index.html', {'nav': 'index'})


def get_articlelist(request):
    blogs = []
    blog_list = Blog.objects.all().order_by('-create_time')
    for blog in blog_list:
        tag_list = []
        tags = blog.tag.all()
        for tag in tags:
            tag_list.append({'tag_id': tag.id, 'tag_name': tag.name})
        blogs.append({
            'id': blog.id,
            'title': blog.title,
            'description': blog.description,
            'create_time': blog.create_time.strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日'),
            'category': blog.category.name,
            'category_id': blog.category.id,
            'tag': tag_list,
            'click_nums': blog.click_nums,
            'cmt_nums': Comment.objects.filter(blog_id=blog.id).count()
        })
    limits = 3
    try:
        page = int(request.GET.get('page'))
        if len(blogs) % limits == 0:
            totals = int(len(blogs) / limits)
        else:
            totals = int(len(blogs) / limits) + 1

        data = blogs[(limits * int(page)) - limits:limits * int(page)]
        blog_info = {
            'paging': {
                'current_page': page,
                'totals': totals
            },
            'data': data,
        }
        return JsonResponse(blog_info)
    except:
        return HttpResponse('error')


def detail(request, article_id):
    article = get_object_or_404(Blog, id=article_id)
    article.click_nums = int(article.click_nums) + 1
    article.save()
    cmt_list = Comment.objects.filter(blog_id=article_id).order_by('-create_time')[:3]
    cmt_nums = cmt_list.count()

    # 实现博客上一篇与下一篇功能
    has_prev = False
    has_next = False
    id_prev = id_next = int(article_id)
    blog_id_max = Blog.objects.all().order_by('-id').first()
    id_max = blog_id_max.id
    while not has_prev and id_prev >= 1:
        blog_prev = Blog.objects.filter(id=id_prev - 1).first()
        if not blog_prev:
            id_prev -= 1
        else:
            has_prev = True
    while not has_next and id_next <= id_max:
        blog_next = Blog.objects.filter(id=id_next + 1).first()
        if not blog_next:
            id_next += 1
        else:
            has_next = True
    extensions = ['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc']
    article_content = markdown.markdown(article.content, extensions=extensions)

    context = {
        'article': article, 'article_content': article_content, 'cmt_list': cmt_list, 'cmt_nums': cmt_nums,
        'blog_prev': blog_prev, 'blog_next': blog_next, 'has_prev': has_prev, 'has_next': has_next,
        'nav': 'detail'
    }
    return render(request, 'detail.html', context=context)


def add_comment(request):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment_form.save()
        return HttpResponse('{"status": "success"}', content_type='application/json')
    else:
        return HttpResponse('{"status": "fail"}', content_type='application/json')


def archive(request):
    post_list = Blog.objects.all().order_by('-create_time')
    return render(request, 'archive.html', context={'post_list': post_list, 'nav': 'archive'})


def category(request, category_id):
    try:
        category = Category.objects.get(id=int(category_id))
        this_category_blogs = Blog.objects.filter(category=category_id)
    except:
        category = Category.objects.get(id=1)
        this_category_blogs = Blog.objects.filter(category=1)
    context = {
        'category': category,
        'blogs': this_category_blogs,
        'nav': 'category'
    }
    return render(request, 'category.html', context=context)


def tag(request, tag_id):
    try:
        tag = Tag.objects.get(id=int(tag_id))
        this_tag_blogs = Blog.objects.filter(tag=tag_id)
    except:
        tag = Tag.objects.get(id=1)
        this_tag_blogs = Blog.objects.filter(tag=1)
    context = {
        'tag': tag,
        'blogs': this_tag_blogs,
        'nav': 'tag'
    }
    return render(request, 'tag.html', context=context)


def about(request):
    return render(request, 'about.html', {'nav': 'aboutme'})


def page_not_found(request):
    return render(request, '404.html')


def page_errors(request):
    return render(request, '500.html')

