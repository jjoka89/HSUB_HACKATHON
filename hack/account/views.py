from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthForm
from board.models import Post
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
#회원가입 폼

def home(request):
    return render(request, 'main.html')

def join(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("당신은 이미 회원입니다."+ str(user.email))
    
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # email = form.cleaned_data.get('email').lower()                        
            username = form.cleaned_data.get('username').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect(destination)
            return redirect("/")
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form']=form
        
    return render(request, 'join.html', context)

def logouts(request):
    logout(request)
    return redirect("/")

def logins(request, *args, **kwargs):
    context={}
    
    user = request.user
    if user.is_authenticated:
        return redirect("/")
    
    destination = get_redirect_if_exists(request)
    if request.POST:
        form = AccountAuthForm(request.POST)
        if form.is_valid():
            # email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            # user = authenticate(email=email, password=password)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if destination:
                    return redirect(destination)
                return redirect("/")
    else:
        form = AccountAuthForm()
        
    context['login_form'] = form
    
    return render(request, 'login.html',context)

def get_redirect_if_exists(request):
    redirect=None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect

def myPage(request):
    user = request.user
    posts = Post.objects.filter(author = user).order_by('-pk')
    
    likes = Post.objects.filter(
        Q(like_users=request.user)
    )
    
    if user.is_authenticated is False:
        return redirect("login")
    
    return render(request, 'myPage.html', 
                {'user': user,
                'posts' : posts,
                'likes' : likes   
                })


@login_required
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('/')
    return render(request, 'delete.html')


