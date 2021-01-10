from django.shortcuts import render, redirect,get_object_or_404
from .models import FileUpload,UserDetails,LikesUser
from django.http import HttpResponse
from .forms import MusicForm, SignUpForm, UserAccountForm,LikeForm, Commentform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib import messages

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import SerializerFileUpload, SerializerUserDetails
User = get_user_model()
# Create your views here.
@login_required(login_url='login')
def MusicList(request):
    try:
        profile = UserDetails.objects.get(user= request.user)
    except:
        profile = UserDetails.objects.create(user=request.user)
    likeUserLikes = LikesUser.objects.filter(name=(request.user))
    likeUserLikesList = []
    for likeUserLike in likeUserLikes:
        likeUserLikesList.append(likeUserLike.user.id)
    # print(likeUserLikesList)
    # Likes Count
    files = FileUpload.objects.all()
    for file in files:
        likeUsers = LikesUser.objects.filter(user=file)
        file.like  = likeUsers.count()
        file.save()
    # likes = Likes.objects.all()
    music = FileUpload.objects.all().order_by('-like')
    if request.method == 'POST':
        form = MusicForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form = MusicForm()
            context = {'musics': music,'form':form,'likeUserLikesList':likeUserLikesList,'profile':profile}
            return redirect('home')
    else:
        form = MusicForm()
        context = {'musics': music,'form':form,'likeUserLikesList':likeUserLikesList,'profile':profile}
    # print(profile)
    return render(request,'play/home.html',context)

def SignUp(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    context = {'form':form}
    return render(request,'play/signup.html',context)

def Login(request):
    name = request.POST.get('name')
    password = request.POST.get('password')
    user = authenticate(request=request,username=name,password=password)
    if user is not None:
        login(request,user)
        return redirect('home')
    else:
        messages.error(request,"Username or password doesn't match")
    return render(request,'play/login.html')

def Logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')

def AccountDetails(request):
    likeUserLikes = LikesUser.objects.filter(name=(request.user))
    likeUserLikesList = []
    for likeUserLike in likeUserLikes:
        likeUserLikesList.append(likeUserLike.user.id)
    print(likeUserLikesList)
    if request.method == 'POST':
        try:
            profile = UserDetails.objects.get(user= request.user)
        except:
            profile = None
        form = UserAccountForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('home')
    else:
        try:
            profile = UserDetails.objects.get(user= request.user)
        except:
            profile = UserDetails.objects.create(user = request.user)
            print('kjhfkhsdkf');
        form = UserAccountForm(instance=profile)
        if profile.profile_image == "":
            profile = ""
    context = {'form':form,'profile':profile}
    return render(request,'play/create_account.html',context)


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def viewLike(request,pk):
    # print(pk)
    if request.method == "POST":
        file = FileUpload.objects.get(id = pk)
        print(file,request.user)
        likesUsers = LikesUser.objects.filter(user = file)
        value = request.POST.get('value')
        print(value)
        username = []
        print(likesUsers)
        for likesUser in likesUsers:
            username.append(likesUser.name.username)
        if value == 'true':
            if str(request.user) not in username:
                LikesUser.objects.create(user=file,name=request.user,status=True).save()
        if value == 'false':
            if str(request.user) in username:
                LikesUser.objects.get(user=file,name=request.user).delete()
    return HttpResponse('Like')

@csrf_exempt
def deleteOption(request,pk):
    if request.method == "POST":
        print(type(pk))
        musicDelete = FileUpload.objects.get(id = pk)
        musicDelete.delete()
    return HttpResponse('delete')


@api_view(['GET'])
def MusicListApi(request):
    musics = FileUpload.objects.all()
    musicsSerialize = SerializerFileUpload(musics,many=True)
    print(musicsSerialize)
    return Response(musicsSerialize.data)


def musicOption(request,pk):
    music = FileUpload.objects.get(id=pk)
    context = {'music': music}
    return render(request,'play/music.html',context)

