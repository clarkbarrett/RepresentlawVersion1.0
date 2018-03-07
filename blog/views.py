from django.utils import timezone
from blog.models import Post, Category
from blog.forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def list_of_post_by_category(request, category_slug):
    categories = Category.objects.all()
    post = Post.objects.filter(status='published')
    paginator = Paginator(post, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        post = post.filter(category=category)
    template = 'blog/list_of_post_by_category.html'
    context = {'categories': categories, 'posts': posts, 'category': category}
    return render(request, template, context)


def list_of_post(request):
    today = timezone.now().date()
    # queryset_list = Post.objects.active()  # .order_by("-published")
    queryset_list = Post.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(seo_title__icontains=query) |
            Q(seo_description__icontains=query) |
            Q(content__icontains=query)
        ).distinct()

    paginator = Paginator(queryset_list, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "posts": queryset,
        "title": "List",
        "page_request_var": page_request_var,
        "today": today
    }
    template = 'blog/list_of_post.html'
    return render(request, template, context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    template = 'blog/post_detail.html'
    context = {'post': post}
    return render(request, template, context)


def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = CommentForm()
    template = 'blog/add_comment.html'
    context = {'form': form}
    return render(request, template, context)


def listing(request):
    contact_list = Post.objects.all()
    paginator = Paginator(contact_list, 2)
    # Show 2 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'website/blog2.html', {'Posts': posts})


def latest_posts(request):
    post = Post.objects.order_by('-published')[0:8]
    template = 'blog/list_of_post.html'
    context = {'posts': post}
    return render(request, template, context)
