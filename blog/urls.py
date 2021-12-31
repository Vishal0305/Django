from django.urls import path,include
from .views import *

app_name='blog'

urlpatterns = [
    path('',home,name="home"),
    path('about-us/',about_us,name="about-us"),
    path('blogs/<int:page>/',blog,name='blogs'),
    path('blogs/create/',blog_create,name='create_blog'),
    path('project/create/',project_create,name='create_project'),
    path('services/',services,name='services'),
    path('portfolio/<int:page>/',portfolio,name='portfolio'),
    path('contact/',contact,name='contact'),
    path('<slug:title>/<int:id>/upload_content',content_upload,name='content_upload'),
    path('project/<int:id>/detail',content_detail,name='content_detail'),
    path('blog/create/<int:id>/detail',blog_detail,name='blog_detail'),
    path('blog/<int:id>/detail',blog_detail_view,name='blog_detail_view')
]