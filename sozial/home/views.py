from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileModelForm, CommentModelForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Post, Comment,Likes, Reply, FollowerCount
from itertools import chain
import random
# Create your views here.
@login_required(login_url='signin')
def index(request):
    all_post = Post.objects.all().reverse()
    user_following_list = []
    feed = []
    user_following = FollowerCount.objects.filter(followed_by= request.user.username)

    for users in user_following:
        user_following_list.append(users.followed_to)
        
    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user__username = usernames)
        feed.append(feed_lists)
    feed_list = list(chain(*feed))
################################################################################################
    all_users = User.objects.all()
    user_following_all = []

    for user in user_following:
        user_list = User.objects.get(username=user.followed_to)
        user_following_all.append(user_list)
    
    new_suggestions_list = [x for x in list(all_users) if (x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(new_suggestions_list) if ( x not in list(current_user))]
    random.shuffle(final_suggestions_list)
    
    username_profile = []
    username_profile_list = []

    for users in final_suggestions_list:
        username_profile.append(users.id)
    
    for ids in username_profile:
        profile_lists = Profile.objects.filter(user__id=ids)
        username_profile_list.append(profile_lists)
    print(username_profile_list)
    suggestions_username_profile_list = list(chain(*username_profile_list))
    print(suggestions_username_profile_list)
    context = {
        'all_post' : feed_list,
        'suggestions_username_profile_list': suggestions_username_profile_list[:4]
    }
    return render(request, 'index.html', context)

def signup(request):
    s_form = SignUpForm()
    if request.method == 'POST':
        s_form = SignUpForm(request.POST)
        if s_form.is_valid():
            s_form.save()
            return redirect('signin')
    else:
        s_form = SignUpForm()
    context = {
        's_form' : s_form
    }
    return render(request, 'signup.html', context)

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('home')



@login_required(login_url='signin')
def profilepage(request, pk):
    user_obj = User.objects.get(username = pk)
    user_profile = Profile.objects.get(user = user_obj)
    post_count = Post.objects.filter(user= user_obj).count
    followed_by = request.user.username
    followed_to = pk
    follower_count = FollowerCount.objects.filter(followed_by= pk).count
    following_count = FollowerCount.objects.filter(followed_to=pk).count

    if FollowerCount.objects.filter(followed_by=followed_by, followed_to=followed_to):
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'
    
    context = {
        'user_obj' : user_obj,
        'user_profile' : user_profile,
        'follower_count': follower_count,
        'following_count': following_count,
        'post_count' : post_count,
        'button_text': button_text
    }
    return render(request, 'profile.html', context)

@login_required(login_url='signin')
def editprofile(request):
    profile_obj = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        pe_form = ProfileModelForm(request.POST, request.FILES, instance=profile_obj)
        if pe_form.is_valid():
            pe_form.save()
            return redirect('home')
        
    else:
        pe_form = ProfileModelForm(instance=profile_obj)


    context = {
        'profile_obj' : profile_obj,
        'pe_form' : pe_form
    }
    return render(request, 'editprofile.html', context)

def posting(request):
    if request.method == 'POST':
        user = request.user
        
        pic = request.FILES['upload']
        body = request.POST.get('body')
        
        p_form = Post(user=user, pic=pic , body=body)
        p_form.save()
        return redirect('home')
    
def comment(request, pk):
    post_inst = Post.objects.get(id = pk)
    c_form = CommentModelForm(instance=post_inst)
    if request.method == 'POST':
        c_form = CommentModelForm(request.POST, instance=post_inst)
        if c_form.is_valid():
            comment_by =  request.user
            comment_body= request.POST.get('comment_body')
            cform = Comment(comment_on=post_inst, comment_by=comment_by, comment_body=comment_body)
            cform.save()
            return redirect('home')
    context= {
        'c_form' : c_form
    }
    return render(request, 'comment.html', context)

def like_post(request):
    liked_by = request.user.username
    like_on = request.GET.get('like_on')
    post = Post.objects.get(id = like_on)
    like_filter = Likes.objects.filter(liked_by=liked_by, like_on=like_on).first()

    if like_filter == None:
        new_like = Likes.objects.create(liked_by=liked_by, like_on=like_on)
        new_like.save()
        post.likes = post.likes + 1
        post.save()
        return redirect('home')
    else:
        like_filter.delete()
        post.likes = post.likes - 1
        post.save()
        return redirect('home')
    
def reply_comment(request, pk):
    reply_inst = Comment.objects.get(id = pk)
    if request.method == 'POST':
        reply_by = request.user
        reply_on = reply_inst
        reply_body = request.POST.get('reply_body')
        rform = Reply(reply_by=reply_by, reply_on=reply_on, reply_body=reply_body)
        rform.save()
        return redirect('home')

def following(request):
    if request.method == 'POST':
        followed_by = request.POST.get('followed_by')
        followed_to = request.POST.get('followed_to')

        if FollowerCount.objects.filter(followed_by=followed_by, followed_to=followed_to).first():
            delete_follower = FollowerCount.objects.get(followed_by=followed_by, followed_to=followed_to)
            delete_follower.delete()
            return redirect('profilepage/' +followed_to)
        else:
            new_follower = FollowerCount.objects.create(followed_by=followed_by, followed_to=followed_to)
            new_follower.save()
            return redirect('profilepage/' +followed_to)
    else:
        return redirect('home')
