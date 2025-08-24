from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

from .models import Post, Category, Ad
from .forms import FeedbackForm, SubscriberForm

# Home view with category filter, search, and pagination
def home(request):
    category_name = request.GET.get('category')
    query = request.GET.get('q')
    posts = Post.objects.all()

    if category_name:
        posts = posts.filter(category__name__iexact=category_name)
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))

    paginator = Paginator(posts.order_by('-date_posted'), 6)  # 6 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    categories = Category.objects.all()

    return render(request, 'blog/home.html', {
        'posts': posts,
        'categories': categories,
        'selected_category': category_name,
        'query': query
    })

# Post detail view with feedback form and related posts
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    feedbacks = post.feedbacks.all().order_by('-submitted_at')
    ads = Ad.objects.all()[:3]
    related_posts = Post.objects.filter(category=post.category).exclude(id=post.id).order_by('?')[:3]

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.post = post
            feedback.save()
            messages.success(request, "Thanks for your feedback!")
            return redirect('post_detail', post_id=post.id)
    else:
        form = FeedbackForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'feedbacks': feedbacks,
        'form': form,
        'ads': ads,
        'related_posts': related_posts
    })

# Newsletter subscription view
def subscribe_newsletter(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully subscribed to our newsletter!')
            return redirect('home')
    else:
        form = SubscriberForm()

    return render(request, 'blog/subscribe.html', {'form': form})
# blog/views.py
from django.shortcuts import render, redirect
from .forms import EnquiryForm
from django.contrib import messages

def submit_enquiry(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your enquiry has been submitted.")
            return redirect(request.META.get('HTTP_REFERER', '/'))
    return redirect('/')


# Static pages
def about(request):
    return render(request, 'blog/about.html')

def services(request):
    return render(request, 'blog/services.html')

def contact(request):
    return render(request, 'blog/contact.html')








