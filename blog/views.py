from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, CommentPost
from django.utils import timezone
from .forms import PostForm, UserRegistrationForm, CommentForm
from django.db.models import Q


# Create your views here.


def post_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) |
 \
                                    Q(text__icontains=search_query))

    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment = CommentPost.objects.filter(post=post, created__lte=timezone.now()).order_by('-created')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.user = request.user
            comm.post = post
            comm.save()
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form,
                                                     'comment': comment})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def dashboard(request):
    return render(request, "blog/dashboard.html")


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'blog/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'blog/register.html', {'user_form': user_form})
