from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse,HttpResponse
from .forms import UserForm, AboutForm, EduForm,TeachingForm,ExperienceForm,TodolistForm
from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import Q
from .models import About,Edu,Teaching,Experience,Todolist
from .new import fetch,name1
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def email(request):
    f = open("category/templates/test.txt","r")
    myList = []
    for line in f:
        myList.append(line)
    l = myList[3].split('"')[1::2];
    print(l[0])
    qs = About.objects.get(user=request.user)
    qs.position=l[0]
    qs.save()
    f.close()
    return redirect('/about/')

def publications(request):
    user = request.session.get('infoo')
    info=get_object_or_404(About,name=user)
    zi=name1(user)
    fi=fetch(user,zi)
    # if not fi:
    #     return render(request,'category/index.html',{'info':info})
    # else:
    return render(request,'category/publications.html',{'fi':fi,'info':info})

def home(request):
    info=About.objects.all()
    return render(request,'category/home.html',{'info' :info})

def todolist(request):
    user = request.session.get('infoo')
    infoo = get_object_or_404(About, name=user)
    info=Todolist.objects.filter(user=request.user)
    return render(request,'category/todo.html',{'info':info,'img':infoo})


def about(request):
    if request.user.is_authenticated():
        info=About.objects.get(user=request.user)
        request.session['infoo'] = info.name
        return render(request, 'category/index.html',{'info':info})
    else:
        return redirect('/login_user/')



def education(request):
    user = request.session.get('infoo')
    info=get_object_or_404(About,name=user)
    eduinfo=Edu.objects.filter(user=info.user)
    return render(request, 'category/education.html', {'info': eduinfo,'img':info})

def experience(request):
    user = request.session.get('infoo')
    info=get_object_or_404(About,name=user)
    eduinfo=Experience.objects.filter(user=info.user)
    return render(request, 'category/experience.html', {'info': eduinfo,'img':info})

def teaching(request):
    user = request.session.get('infoo')
    info=get_object_or_404(About,name=user)
    teachinginfo2=Teaching.objects.filter(user=info.user)
    if not teachinginfo2:
         return render(request, 'category/teaching.html', {'current': teachinginfo2, 'past': teachinginfo2, 'img': info})
    else:
        current = Teaching.objects.filter(user=info.user).filter(currentorpast="Current")
        past = Teaching.objects.filter(user=info.user).filter(currentorpast="Past")
        #teachinginfo = get_object_or_404(Teaching, user=info.user)
        #current=teachinginfo.objects.filter(currentorpast="Current")
        #past=teachinginfo.objects.filter(currentorpast="Past")
        return render(request, 'category/teaching.html', {'current': current,'past': past, 'img': info})

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'category/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/about/')
            else:
                return render(request, 'category/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'category/login.html', {'error_message': 'Invalid login'})
    return render(request, 'category/login.html')


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        # form.email = request.POST['Email']
        # form.password = request.POST['password']
        # form.username = request.POST['username']
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #info = About.objects.filter(user=request.user)
                    return redirect('/createabout/')
    return render(request, 'category/registerform.html')

def createabout(request):
    if not request.user.is_authenticated():
        return render(request, 'category/login.html')
    else:
        form = AboutForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            info = form.save(commit=False)
            info.user = request.user
            info.image = request.FILES['image']
            file_type = info.image.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'info': info,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'category/aboutform.html', context)
            info.save()
            return redirect('/about/')
        context = {
            "form": form,
        }
        return render(request, 'category/aboutform.html', context)

def createtodo(request):
    if not request.user.is_authenticated():
        return render(request, 'category/login.html')
    else:
        form = TodolistForm(request.POST or None)
        if form.is_valid():
            info = form.save(commit=False)
            info.user = request.user
            info.save()
            return redirect('/todolist/')
        context = {

            "form": form,
        }
        return render(request, 'category/register.html', context)

def createeducation(request):
    if not request.user.is_authenticated():
        return render(request, 'category/login.html')
    else:
        form = EduForm(request.POST or None)
        if form.is_valid():
            info = form.save(commit=False)
            info.user = request.user
            info.save()
            return redirect('/education/')
        context = {
            "form": form,
        }
        return render(request, 'category/register.html', context)

def createexperience(request):
    if not request.user.is_authenticated():
        return render(request, 'category/login.html')
    else:
        form = ExperienceForm(request.POST or None)
        if form.is_valid():
            info = form.save(commit=False)
            info.user = request.user
            info.save()
            return redirect('/experience/')
        context = {
            "form": form,
        }
        return render(request, 'category/register.html', context)


def addteaching(request):
    if not request.user.is_authenticated():
        return render(request, 'category/login.html')
    else:
        form = TeachingForm(request.POST or None)
        if form.is_valid():
            info = form.save(commit=False)
            info.user = request.user
            info.save()
            return redirect('/teaching/')
        context = {
            "form": form,
        }
        return render(request, 'category/register.html', context)

def editabout(request):
    info = get_object_or_404(About, user=request.user)
    if request.method == "POST":
        form = AboutForm(request.POST or None, request.FILES or None, instance=info)
        if form.is_valid():
            info = form.save(commit=False)
            info.user = request.user
            info.save()
            return redirect('/about/')
    else:
        form = AboutForm(instance=info)
    return render(request, 'category/aboutform.html', {'form': form})

# def editeducation(request):
#     user = request.session.get('infoo')
#     info = get_object_or_404(About, name=user)
#     eduinfo = get_object_or_404(Edu,user=info.user)
#     if request.method == "POST":
#         form = EduForm(request.POST or None, instance=eduinfo)
#         if form.is_valid():
#             eduinfo = form.save(commit=False)
#             eduinfo.user = request.user
#             eduinfo.save()
#             return redirect('/education/')
#     else:
#         form = EduForm(instance=eduinfo)
#     return render(request, 'category/register.html', {'form': form})

def aboutto(request,user_name):
    infoo=get_object_or_404(About,name=user_name)
    request.session['infoo'] = infoo.name
    return render(request, 'category/index.html', {'info': infoo})

def deleteedu(request,pk):
    instance = Edu.objects.get(id=pk)
    instance.delete()
    return redirect('/education/')

def deleteexperience(request,pk):
    instance = Experience.objects.get(id=pk)
    instance.delete()
    return redirect('/experience/')

def deleteteaching(request,pk):
    instance = Teaching.objects.get(id=pk)
    instance.delete()
    return redirect('/teaching/')

def deletetodo(request,pk):
    instance = Todolist.objects.get(id=pk)
    instance.delete()
    return redirect('/todolist/')











