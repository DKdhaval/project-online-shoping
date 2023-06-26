from django.shortcuts import render,redirect
from management.views import slider,services,blogcategory,blog
from yomapp.models import comments,commentsform,Contact,Contactform,Workcategory,Workcategoryform,Work,Workform,Clients,Clientsform


# Create your views here.

def index(request):
    # if 'adminid' not in request.session:
    #     return redirect('/adminlogin/')
    slider1 = slider.objects.filter().all()
    services1 = services.objects.order_by('-id')[:3].all()
    blogcategory1 = blogcategory.objects.filter().all()
    workcategory1 = Workcategory.objects.filter().all()
    blog1 = blog.objects.order_by('-id')[:3].all()
    comment1 = comments.objects.order_by('-id')[:9].all()
    blog5 = blog.objects.order_by('-id')[:5].all()
    Work8 = Work.objects.order_by('-id')[:8].all()
    blogcategory1 = blogcategory.objects.filter().all()
    return render(request, 'index.html' , {'slider_detail' : slider1 , 'services_detail' : services1 , 'blogcategory_detail' : blogcategory1 , 'blog_detail' : blog1 ,'blog5_detail':blog5,'comment_detail':comment1,'workcategory_detail':workcategory1,'work8':Work8})


def about(request):
    blog5 = blog.objects.order_by('-id')[:5].all()
    blogcategory1 = blogcategory.objects.filter().all()
    workcategory1 = Workcategory.objects.filter().all()
    clients1 = Clients.objects.filter().all()
    return render(request,'about.html',{'blogcategory_detail' : blogcategory1  ,'blog5_detail':blog5,'workcategory_detail':workcategory1,'clients_detail':clients1})

def blog1(request,Cat_id):
    blog2 = blog.objects.filter(Cat_id_id=Cat_id).all()
    blog5 = blog.objects.order_by('-id')[:5].all()
    blogcategory1 = blogcategory.objects.filter().all()
    workcategory1 = Workcategory.objects.filter().all()
    return render(request,'blog.html',{'blogcategory_detail' : blogcategory1 , 'blog2':blog2 ,'blog5_detail':blog5,'workcategory_detail':workcategory1})

def bloggrid(request):
    blog5 = blog.objects.order_by('-id')[:5].all()
    blog_all = blog.objects.filter().all()
    blogcategory1 = blogcategory.objects.filter().all()
    workcategory1 = Workcategory.objects.filter().all()
    return render(request,'blog-grid.html',{'blogcategory_detail' : blogcategory1  ,'blog5_detail':blog5,'workcategory_detail':workcategory1,'blog_all':blog_all})

def blogsingle(request,Blog_id):
    blog_show = blog.objects.filter(id=Blog_id).get()
    blog_comment = comments.objects.filter(Blogid_id = Blog_id).all()
    workcategory1 = Workcategory.objects.filter().all()
    blog5 = blog.objects.order_by('-id')[:5].all()
    blog1 = blog.objects.order_by('-id')[:3].all()
    # quary = request.POST['S1']
    blogsearch = blog.objects.filter(Tital__contains = "F").all()
    blogcategory1 = blogcategory.objects.filter().all()
    obj = commentsform()
    if 'save' in request.POST:
        obj = commentsform(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
            msg = "Successfull"
    return render(request,'blog-single.html',{'blogcategory_detail' : blogcategory1 ,'blog_show':blog_show ,'blog_detail':blog1,'Comments_detail':blog_comment ,'blog5_detail':blog5,'workcategory_detail':workcategory1})

def clients(request):
    blog5 = blog.objects.order_by('-id')[:5].all()
    blogcategory1 = blogcategory.objects.filter().all()
    clients1 = Clients.objects.filter().all()
    workcategory1 = Workcategory.objects.filter().all()
    return render(request,'clients.html',{'blogcategory_detail' : blogcategory1  ,'blog5_detail':blog5,'workcategory_detail':workcategory1,'clients_detail':clients1})

def contact1(request):
    blog5 = blog.objects.order_by('-id')[:5].all()
    blogcategory1 = blogcategory.objects.filter().all()
    workcategory1 = Workcategory.objects.filter().all()
    contact1 = Contact.objects.filter().all()
    obj = Contactform()
    if 'save' in request.POST:
        obj = Contactform(request.POST)
        if obj.is_valid():
            obj.save()
            msg = "Successfull"
            return redirect('/contact/')
    return render(request,'contact.html',{'blogcategory_detail' : blogcategory1 ,'contact_detail' :contact1 ,'blog5_detail':blog5,'workcategory_detail':workcategory1 })

def services1(request):
    blog5 = blog.objects.order_by('-id')[:5].all()
    services2 = services.objects.filter().all()
    workcategory1 = Workcategory.objects.filter().all()
    blogcategory1 = blogcategory.objects.filter().all()
    return render(request,'services.html',{'blogcategory_detail' : blogcategory1 ,'services_detail':services2 ,'blog5_detail':blog5,'workcategory_detail':workcategory1})

def singleproject(request):
    blog5 = blog.objects.order_by('-id')[:5].all()
    workcategory1 = Workcategory.objects.filter().all()
    blogcategory1 = blogcategory.objects.filter().all()
    return render(request,'single-project.html',{'blogcategory_detail' : blogcategory1 ,'blog5_detail':blog5,'workcategory_detail':workcategory1})


def work3columns(request):
    blog5 = blog.objects.order_by('-id')[:5].all()
    workcategory1 = Workcategory.objects.filter().all()
    Work1 = Work.objects.filter().all()
    blogcategory1 = blogcategory.objects.filter().all()
    return render(request,'work-3columns.html',{'blogcategory_detail' : blogcategory1 ,'blog5_detail':blog5,'workcategory_detail':workcategory1,'Work_detail':Work1 })

def work4columns(request):
    blog5 = blog.objects.order_by('-id')[:5].all()
    workcategory1 = Workcategory.objects.filter().all()
    blogcategory1 = blogcategory.objects.filter().all()
    Work1 = Work.objects.filter().all()
    return render(request,'work-4columns.html',{'blogcategory_detail' : blogcategory1 ,'blog5_detail':blog5,'workcategory_detail':workcategory1,'Work_detail':Work1})

def search(request):
    search_word = request.GET['keyword']
    blogsearch = blog.objects.filter(Tital__contains = search_word).all()
    # blogsearch = blogcategory.objects.filter(Name__contains = search_word).all()
    blog5 = blog.objects.order_by('-id')[:5].all()
    workcategory1 = Workcategory.objects.filter().all()
    blogcategory1 = blogcategory.objects.filter().all()
    Work1 = Work.objects.filter().all()
    return render(request,'search.html',{'blogcategory_detail' : blogcategory1 ,'blog5_detail':blog5,'workcategory_detail':workcategory1,'Work_detail':Work1,'Blog_Search':blogsearch})


def view_comment(request):
    slider1 = comments.objects.filter().all()
    print(slider1)
    return render(request, 'comment_view.html' , {'Comments_view' : slider1 })

def view_contact(request):
    slider1 = Contact.objects.filter().all()
    print(slider1)
    return render(request, 'comment_view.html' , {'Comments_view' : slider1 })


def delete_comment_view(request,del_id):
    comments.objects.get(id=del_id).delete()
    return redirect('/commentview/')

def delete_contact_view(request,del_id):
    Contact.objects.get(id=del_id).delete()
    return redirect('/contact/')



# def TweenLite(request):
#     return render(request,'TweenLite.html')
