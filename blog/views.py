from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth import views as auth_views, login
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import *


class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('blog:login')
    template_name = None


@login_required
def post_list_view(request):
    post_list =  Post.objects.order_by('-created_date')
    return render(request, 'blog/postlist.html', {'post_list': post_list, })


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/postdetail.html', {'post': post, })


def write_post_view(request):
    if request.method == 'POST':
        post = Post()
        post.author = request.user
        post.content = request.POST.get('content')
        post.title = request.POST.get('title')
        post.save()
        return redirect('blog:list')
    return render(request, 'blog/writepost.html', )


def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:list')


def post_update_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('blog:list')
    return render(request, 'blog/updatepost.html', {'post': post, })


def new_comment_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment = Comment()
    comment.post = post
    comment.author = request.user
    comment.text = request.POST.get('text')
    print(comment.text)
    comment.save()
    return redirect('blog:post_detail', pk=post.pk)


def comment_remove_view(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blog:post_detail', pk=comment.post.pk)


def mypage_view(request):
    return render(request, 'blog/mypage.html', )


def change_avatar_view(request):
    avatar = request.FILES['avatar']
    print(avatar)
    request.user.avatar = avatar
    request.user.save()
    return render(request, 'blog/mypage.html', )


def signup_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = MyUser.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('blog:list')
    else:
        form = UserForm()
    return render(request, 'blog/signup.html', {'form':form})


def signout_view(request):
    user = request.user
    user.delete()
    return redirect('index')