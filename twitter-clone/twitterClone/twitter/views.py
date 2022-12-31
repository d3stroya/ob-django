from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # preguardamos el tuit
            post = form.save(commit=False)
            # accedemos al usuario que está tuiteando
            post.user = request.user
            # guardamos el tuit
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    context = {'posts': posts, 'form': form}
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()

    context = {'form': form}        
    return render(request, 'forms/register.html', context)

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('home')

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    posts = user.posts.all()
    context = {'user': user, 'posts': posts}
    return render(request, 'profile.html', context)

def edit(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm()

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'edit.html', context)

def follow(request, username):
    current_user = request.user
    to_user_id = User.objects.get(username=username)
    rel = Relationship(from_user=current_user, to_user = to_user_id)
    rel.save()
    return redirect('home')

def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    rel = Relationship.objects.get(from_user=current_user.id, to_user=to_user.id)
    rel.delete()
    return redirect('home')