from django.shortcuts import render

from django.http import HttpResponse

from blog.models import Article

# 1、导入分页组件Paginator
from django.core.paginator import Paginator
# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World!")


def article_content(request):
    article = Article.objects.all()[0]
    article_title = article.article_title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = 'article_title:%s,brief_content:%s,' \
                 'content:%s,article_id:%s,publish_date:%s' % (
                 article_title, brief_content, content, article_id, publish_date)
    return HttpResponse(return_str)


def get_index_page(request):
    page = request.GET.get('page')  # 从url中获取当前页
    if page:
        page = int(page)
    else:
        page = 1
    # print(page)
    all_article = Article.objects.all()
    # 按照publish_date倒序排序，并取前五篇
    top5_article_list=Article.objects.order_by('-publish_date')[:5]

    # 2、创建分页对象，通过该对象来调用分页的所有属性 ，
    paginator = Paginator(all_article, 3)  # 设置每页显示几条，此处为3条
    page_num = paginator.num_pages  # page_nums 分页数量
    print('page num ', page_num)
    page_article_list = paginator.page(page)  # 到指定页取值
    if page_article_list.has_next():
        next_page = page+1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page-1
    else:
        previous_page = page
    # 自动搜索templates下边的blog/index.html
    # range(start, end, step)，返回一个list对象，起始值为start，终止值为end，但不含终止值，步长为step。只能创建int型list。
    return render(request, 'blog/index.html', {
        'article_list': page_article_list,
        'page_num': range(1, page_num+1),   # 分页总数
        'cur_page': page,  # 当前页
        'next_page': next_page,   # 下一页
        'previous_page': previous_page,  # 上一页
        'top5_article_list': top5_article_list
    })


def get_detail_page(request, article_id):
    all_article = Article.objects.all()
    cur_article = None
    previous_index = 0
    next_index = 0
    previous_article = None
    next_article = None
    for index, article in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index+1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.article_id == article_id:
            cur_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break
    section_list = cur_article.content.split('\n')
    # 自动搜索templates下边的blog/detail.html
    return render(request, 'blog/detail.html', {
        'cur_article': cur_article,
        'section_list': section_list,
        'previous_article': previous_article,
        'next_article': next_article
    })
    pass
