from urllib.request import Request
import django
from django.shortcuts import redirect, render
from .models import Post,StudentUser,Contact,Service,Purchase
from infoapp.forms import BlogPost
# from infoapp.forms import BlogPost
from datetime import date
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from ckeditor.fields import RichTextField

# Create your views here.

# index section
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        msg=request.POST['msg']

        contact=Contact.objects.create(fname=fname,lname=lname,email=email,msg=msg)
        contact.save()
        messages.info(request,'You have Contact Successfully')
        
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def service(request):
    services=Service.objects.all()
    context={
        'services':services
    }
    return render(request,'service.html',context)

def service_details(request,slug):
    services=Service.objects.filter(slug=slug)
    context={
        'services':services
    }
    return render(request,'service_details.html',context)

def purchase(request):
    if request.method=="POST":
        name=request.POST['name']
        foundation=request.POST['foundation']
        email=request.POST['email']
        pdf1=request.FILES['pdf1']
       
        for i in pdf1:
            purchase=Purchase.objects.create(name=name,foundation=foundation,email=email,pdf1=pdf1)
            purchase.save()
        
        messages.info(request,'You have Submitted Successfully')
        return redirect('purchase')

    return render(request,'purchase.html')

def team(request):
    return render(request,'team.html')

# login
def userlogin(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
           
            user1 = StudentUser.objects.get(user=user)
      
            if user1.type == "user":
                login(request, user)
                messages.success(request, 'Successfully logged In')
                return redirect("post_list")

            else:
                messages.info(request, 'This is not Registered')
                return redirect('usersignup')

        else:
            messages.info(request, 'Check username or Password')
            return redirect('userlogin')

    return render(request,'userlogin.html')

# blog section
def blog(request):
    post=Post.objects.order_by('-date')
     # for pagination
    paginator=Paginator(post,15)
    page_number=request.GET.get('page')
    postfinal=paginator.get_page(page_number)
    totalpage=postfinal.paginator.num_pages
    context={
        'post':postfinal,
        'lastpage':totalpage,
        'totalpagelist':[ n+1 for n in range(totalpage) ]
        }
   
    return render(request,'blog.html',context)


# blog details
def blog_details(request,slug):
    post=Post.objects.filter(slug=slug)
    context={
        'post':post
    }
    return render(request,'blog_details.html',context)

def userpost_details(request,slug):
    post=Post.objects.filter(slug=slug)
    context={
        'post':post
    }
    return render(request,'userpost_details.html',context)

# add post section
def add_post(request):
    post=Post.objects.all()
    context={
        'post':post
    }
    if request.method=="POST":
        title=request.POST['title']
        image=request.FILES['image']
        # blogger=request.POST['blogger']
        desc=request.POST['desc']
        user=request.user
        studentuser=StudentUser.objects.get(user=user)

        addpost=Post.objects.create(author=studentuser,title=title,image=image,desc=desc,date=date.today())
        addpost.save()
        messages.info(request,'successfully add post ')
        return redirect('add_post')
    return render(request,'add_post.html',context)

# testing
def add_post2(request):
    if request.method=='POST':
        fm=BlogPost(request.POST,files=request.FILES)
        if fm.is_valid():
            author=fm.cleaned_data['author']
            title=fm.cleaned_data['title']
            desc=fm.cleaned_data['desc']
            image=fm.cleaned_data['image']
            post=Post(author=author,title=title,image=image,desc=desc)
            fm.save()
            messages.info(request,'Successfully add post')
            
            fm=BlogPost()
            return redirect('add_post2')
    else:
        fm=BlogPost()
    post=Post.objects.all()
    return render(request,'add_post2.html',{'form':fm,'post':post})
# user post list
def post_list(request,):
    user=request.user
    studentuser=StudentUser.objects.get(user=user)
    post=Post.objects.filter(author=studentuser)
      # for pagination
    paginator=Paginator(post,15)
    page_number=request.GET.get('page')
    postfinal=paginator.get_page(page_number)
    totalpage=postfinal.paginator.num_pages
    context={
        'post':postfinal,
        'lastpage':totalpage,
        'totalpagelist':[ n+1 for n in range(totalpage) ]
        }
    
    return render(request,'post_list.html',context)

# edit post
def edit_post(request,id):
    post=Post.objects.get(id=id)
    
    if request.method=="POST":
        title=request.POST['title']
        blogger=request.POST['blogger']
        desc=request.POST['desc']

        post.title=title
        post.blogger=blogger
        post.desc=desc
        post.save()
       
        messages.info(request,'Successfully edit post Details')
        return redirect('post_list')
    context={
        'post':post
    }
    return render(request,'edit_post.html',context)

def edit_post2(request,id):
    # post=Post.objects.get(id=id)
    
    if request.method=='POST':
        pi=Post.objects.get(id=id)
        fm=BlogPost(request.POST, instance=pi,files=request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        pi=Post.objects.get(id=id)
        fm=BlogPost(instance=pi)
        messages.info(request,'Updated Sucessfully')

    context={
        'form':fm

    }
    return render(request,'edit_post2.html',context)

# change post image
def changeimage(request,id):
    post=Post.objects.get(id=id)
    if request.method == "POST":
        image= request.FILES['image']
        post.image=image
        post.save()
        messages.info(request,'Image Successfully changed')
    context={
        'post':post
    }
    return render(request,'changeimage.html',context)

# delete_post
def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('post_list')

# user registeration
def usersignup(request):
    if request.method == "POST":
        username = request.POST['username']
        # email= request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken")
            return redirect("usersignup")


        if pass1 != pass2:
            messages.info(request, "Password do not matched")
            return redirect("usersignup")

        
        user = User.objects.create_user(
            username=username, password=pass1)
        StudentUser.objects.create(
            user=user,  type="user")

        messages.success(request, "User Created")
        return redirect("userlogin")

    return render(request,'usersignup.html')

def userlogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')
