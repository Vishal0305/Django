from django.db.models.fields import EmailField
from django.shortcuts import redirect, render
from .models import Blog,Project,Contact,ProjectContent,ProjectMedia,BlogDetail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,JsonResponse
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt
import json
from slugify import slugify


# Create your views here.

def home(request):
    return render(request,'services.html')

    
def about_us(request):
    return render(request,'aboutus.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method=='POST':
        check = Contact.objects.filter(email=request.POST['email'])
        if not check:
            contact = Contact.objects.create(name=request.POST['name'],email=request.POST['email'],phone=request.POST['mobile'],message=request.POST['message'])
    return render(request,'contact.html')

def content_detail(request,id=None):
    if not id or not Project.objects.filter(id=id):
        return HttpResponse('<h1>Invalid Project</h1>')
    project = Project.objects.get(id=id)
    print(project)
    media_content = project.media_content.all()
    text_content = project.text_content.all()
    print(media_content)
    return render(request,'projects/project_type_1.html',{'project':project,'media_contents':media_content,'text_contents':text_content})

def blog_detail_view(request,id=None):
    if not id or not Project.objects.filter(id=id):
        return HttpResponse('<h1>Invalid Project</h1>')
    blog=Blog.objects.get(id=id)
    detail=blog.detail.all()
    print(detail)
    return HttpResponse('<h1>Blog Content</h1>')

def blog_detail(request,id=None):
    if id is None or not Blog.objects.filter(id=id):
        return HttpResponse('<h1>Invalid Project</h1>')
    if request.method=='POST':
        blog = Blog.objects.get(id=id)
        detail = BlogDetail.objects.create(Blog=blog,content1=request.POST['content1'],content2=request.POST['content2'],content3=request.POST['content3'],content3_title=request.POST['content3_title'],content4=request.POST['content4'],content4_title=request.POST['content4_title'],image=request.FILES['image'],video=request.FILES['video'])
        return render(request,'blog_detail_view.html',{'blog':blog,'detail':detail})
    return render(request,'blog_detail.html')

def blog(request,**kwargs):
    blogs = Blog.objects.all()
    page = kwargs['page']
    paginator = Paginator(blogs, 3)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request,'blogs.html',{'blogs':blogs})

@csrf_exempt
def content_upload(request,title,id=None):
    if id is None:
        return HttpResponse('Invalid project')
    if not Project.objects.filter(id=id):
        return HttpResponse('<h1>Project Does not exist</h1>')
    project = Project.objects.get(id=id)
    print(request.FILES)
    print(request.POST)
    if request.user.is_authenticated:
        if request.method=='POST':
            type = request.POST['template_type']
            if type=='Type1':
                for i in range(1,7):
                    print(request.POST[f'image{i}'])
                    if request.POST[f'image{i}']=="true":
                        ProjectMedia.objects.create(project=project,image=request.FILES[f'image{i}_input'])
                    else:
                        ProjectMedia.objects.create(project=project,video=request.FILES[f'video{i}_input'],is_photo=False)
                for i in range(1,6):
                    ProjectContent.objects.create(project=project,text=request.POST[f'text{i}_input'])
            elif type=='Type2':
                project.type = 2
                project.save()
                for i in range(1,10):
                    if request.POST[f'image{i}']=="true":
                        ProjectMedia.objects.create(project=project,image=request.FILES[f'image{i}_input'])
                    else:
                        ProjectMedia.objects.create(project=project,video=request.FILES[f'video{i}_input'],is_photo=False)
                for i in range(1,6):
                    ProjectContent.objects.create(project=project,text=request.POST[f'text{i}_input'])
            else:
                project.type=3
                project.save()
                for i in range(1,8):
                    if request.POST[f'image{i}']=="true":
                        ProjectMedia.objects.create(project=project,image=request.FILES[f'image{i}_input'])
                    else:
                        ProjectMedia.objects.create(project=project,video=request.FILES[f'video{i}_input'],is_photo=False)
                for i in range(1,5):
                    ProjectContent.objects.create(project=project,text=request.POST[f'text{i}_input'])
            print("hello")
            return JsonResponse({'id':id})
        return render(request,'content_upload.html')
    return HttpResponse('<h1>You are not logged in! Please log in to continue</h1>')


def portfolio(request,**kwargs):
    if 'category' not in request.GET:
        projects = Project.objects.all()
    else:
        category = request.GET['category']
        projects = Project.objects.filter(category=category)
    page = kwargs['page']
    paginator = Paginator(projects, 5)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    return render(request,'portfolio.html',{'projects':projects})

def blog_create(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            if 'video' in request.FILES:
                print('In video')
                blog = Blog.objects.create(title=request.POST['title'],content=request.POST['content'],video=request.FILES['video'],is_photo=False)
            else:
                print('in photo')
                print(request.FILES)
                blog = Blog.objects.create(title=request.POST['title'],content=request.POST['content'],image=request.FILES['image'])
            return redirect('blog:blog_detail',id=blog.id)
        return render(request,'create_blog.html')
    return HttpResponse('<h1>You are not logged in! Please log in to continue</h1>')

def project_create(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            if 'video' in request.FILES:
                print('In video')
                project = Project.objects.create(title=request.POST['title'],content=request.POST['content'],video=request.FILES['video'],category=request.POST['category'],is_photo=False)
            else:
                print('in photo')
                print(request.FILES)
                project = Project.objects.create(title=request.POST['title'],content=request.POST['content'],image=request.FILES['image'],category=request.POST['category'])
            return redirect('blog:content_upload',title= slugify(request.POST['title']),id=project.id)
        return render(request,'create_project.html')
    return HttpResponse('<h1>You are not logged in! Please log in to continue</h1>')

