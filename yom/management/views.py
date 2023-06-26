from django.shortcuts import render,redirect
from management.models import admin1,admin1form,slider,sliderform,services,servicesform,blogcategory,blogcategoryform,blog,blogform
from yomapp.models import Contact,comments,Workcategory,Workcategoryform,Work,Workform,Clients,Clientsform
from django.http import HttpResponse
# Create your views here.



def adminregistration(request):
    msg = ""
    obj = admin1form()
    if 'save' in request.POST:
        obj = admin1form(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
            msg = "Successfull"
            return redirect('/adminlogin/')
    return render(request,'admin-register-v2.html',{'msg':msg,'frm':obj})

def login(request):
    msg = ""
    if 'login' in request.POST:
        email = request.POST['Email']
        password = request.POST['Password']
        rows = admin1.objects.filter(Email=email,Password=password)
        print(rows.count())
        if rows.count() == 0:
            msg = "Invalid E-Mail Or Password"
        else:
            user = rows.first()
            request.session['adminid'] = user.id
            print(user)
            msg = "Success"
            return redirect("/adminwelcome/")
    return render(request,'admin-login-v2.html',{'msg':msg})

def welcome(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request , 'admin-index.html', {'info':info})

# ------------------------------------------------------------------------------ Admin ------------

def adminaddregistration(request):
    msg = ""
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    obj = admin1form()
    if 'save' in request.POST:
        obj = admin1form(request.POST,request.FILES)
        obj.save()
        msg = "Successfull"
        return redirect('/admindata/')
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request,'admin-general.html',{'msg':msg ,'info':obj , 'info':info})

def view_admin(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    admin = admin1.objects.filter().all()
    print(admin)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-data.html' , {'info1' : admin , 'info':info}) 

def edit_profile(request,edit_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    info=admin1.objects.filter(id=edit_id).get()
    obj=admin1form(instance=info)
    msg=""
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    else:
        if 'save' in request.POST:
            obj=admin1form(request.POST,request.FILES,instance=info)
            if obj.is_valid():
                obj.save()
                msg="data update"
                return redirect("/admindata/")
            print(info)
    return render(request,'admin-general.html',{'edit_profile':info,'msg':msg})

def delete_admin_view(request,del_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    admin1.objects.get(id=del_id).delete()
    return redirect('/admindata/')

# ----------------------------------------------------------------------------- Slider ------------

def adminslider(request):
    msg = ""
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    obj = sliderform()
    if 'save' in request.POST:
        obj = sliderform(request.POST,request.FILES)
        obj.save()
        msg = "Successfull"
        return redirect('/viewslider/')
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request,'admin-add-slider.html',{'msg':msg , 'info':info})

def view_slider(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    slider1 = slider.objects.filter().all()
    print(slider1)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-view-slider.html' , {'slider_detail' : slider1 , 'info':info})

def edit_slider(request,edit_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    info=slider.objects.filter(id=edit_id).get()
    obj=sliderform(instance=info)
    msg=""
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    else:
        if 'save' in request.POST:
            obj=sliderform(request.POST,request.FILES,instance=info)
            if obj.is_valid():
                obj.save()
                msg="data update"
                return redirect("/viewslider/")
            print(info)
    return render(request,'admin-add-slider.html',{'edit_Slider':info,'msg':msg})

def delete_slider_view(request,del_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    slider.objects.get(id=del_id).delete()
    return redirect('/viewslider/')

# --------------------------------------------------------------------------- Services ------------

def adminservices(request):
    msg = ""
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    obj = servicesform()
    if 'save' in request.POST:
        obj = servicesform(request.POST,request.FILES)
        obj.save()
        msg = "Successfull"
        return redirect('/viewservices/')
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request,'admin-add-services.html',{'msg':msg , 'info':info})

def view_services(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    services1 = services.objects.filter().all()
    print(services1)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-view-services.html' , {'services_detail' : services1 , 'info':info})

def edit_services(request,edit_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    info=services.objects.filter(id=edit_id).get()
    obj=servicesform(instance=info)
    msg=""
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    else:
        if 'save' in request.POST:
            obj=servicesform(request.POST,request.FILES,instance=info)
            if obj.is_valid():
                obj.save()
                msg="data update"
                return redirect("/viewservices/")
            print(info)
    return render(request,'admin-add-services.html',{'edit_Services':info,'msg':msg})

def delete_services_view(request,del_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    services.objects.get(id=del_id).delete()
    return redirect('/viewservices/')

# ---------------------------------------------------------------------- Blog Category ------------

def adminblogcategory(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    msg = ""
    obj = blogcategoryform()
    if 'save' in request.POST:
        obj = blogcategoryform(request.POST,request.FILES)
        obj.save()
        msg = "Successfull"
        return redirect('/viewblogcategory/')
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request,'admin-add-blogcategory.html',{'msg':msg  , 'info':info})

def view_blogcategory(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    blogcategory1 = blogcategory.objects.filter().all()
    print(blogcategory1)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-view-blogcategory.html' , {'blogcategory_deatil' : blogcategory1 , 'info':info})

def edit_blogcategory(request,edit_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    info=blogcategory.objects.filter(id=edit_id).get()
    obj=blogcategoryform(instance=info)
    msg=""
    if 'save' in request.POST:
        obj=blogcategoryform(request.POST,request.FILES,instance=info)
        if obj.is_valid():
            obj.save()
            msg="data update"
            return redirect("/viewblogcategory/")
        print(info)
    return render(request,'admin-add-blogcategory.html',{'Blog_Category':info,'msg':msg})

def delete_blogcategory_view(request,del_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    blogcategory.objects.get(id=del_id).delete()
    return redirect('/viewblogcategory/')

# ------------------------------------------------------------------------------- Blog ------------

def adminblog(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    msg = ""
    all_cat = blogcategory.objects.all()
    obj = blogform()
    if 'save' in request.POST:
        obj = blogform(request.POST,request.FILES)
        obj.save()
        msg = "Successfull"
        return redirect('/viewblog/')
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request,'admin-add-blog.html',{'msg':msg , 'info':info , 'all_cats':all_cat})

def view_blog(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    blog1 = blog.objects.filter().all()
    print(blog1)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-view-blog.html' , {'blog_deatil' : blog1 , 'info':info})

def edit_blog(request,edit_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    adminid = request.session['adminid']
    info2 = admin1.objects.filter(id=adminid).get()
    all_cat = blogcategory.objects.all()
    info=blog.objects.filter(id=edit_id).get()
    obj=blogform(instance=info)
    msg=""
    if 'update' in request.POST:
        obj=blogform(request.POST,request.FILES,instance=info)
        if obj.is_valid():
            obj.save()
            msg="data update"
            return redirect("/viewblog/")
        print(info)
    return render(request,'admin-edit-blog.html',{'Blog':info,'msg':msg,'all_cats':all_cat,'info2':info2})

def delete_blog_view(request,del_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    blog.objects.get(id=del_id).delete()
    return redirect('/viewblog/')

#  ------------------------------------------------------------------ Contact ----------

def view_contact(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    contact1 = Contact.objects.filter().all()
    print(contact1)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-view-contact.html' , {'contact_detail' : contact1 , 'info':info})


def view_comment(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    comment1 = comments.objects.filter().all()
    print(comment1)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-view-comment.html' , {'comment_deatil' : comment1 , 'info':info})


# ---------------------------------------------------------------------- Work Category ------------

def adminworkcategory(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    msg = ""
    obj = Workcategoryform()
    if 'save' in request.POST:
        obj = Workcategoryform(request.POST)
        obj.save()
        msg = "Successfull"
        return redirect('/viewworkcategory/')
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request,'admin-add-workcategory.html',{'msg':msg  , 'info':info})

def view_workcategory(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    workcategory1 = Workcategory.objects.filter().all()
    print(workcategory1)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-view-workcategory.html' , {'workcategory_deatil' : workcategory1 , 'info':info})

def edit_workcategory(request,edit_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    info=Workcategory.objects.filter(id=edit_id).get()
    obj=Workcategoryform(instance=info)
    msg=""
    if 'save' in request.POST:
        obj=Workcategoryform(request.POST,instance=info)
        if obj.is_valid():
            obj.save()
            msg="data update"
            return redirect("/viewworkcategory/")
        print(info)
    return render(request,'admin-add-workcategory.html',{'Work_Category':info,'msg':msg})

def delete_workcategory_view(request,del_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    Workcategory.objects.get(id=del_id).delete()
    return redirect('/viewworkcategory/')


# ------------------------------------------------------------------------------- Work ------------

def adminwork(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    msg=""
    all_work_cat = Workcategory.objects.all()
    obj = Workform()
    if 'save' in request.POST:
        obj = Workform(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
            msg = "Success"
            return redirect('/viewwork/')
    adminid = request.session['adminid']
    info = admin1.objects.filter(id = adminid).get()
    return render(request,'admin-add-work.html',{'msg':msg,'info':info,'all_work_cat':all_work_cat})


def view_work(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    Work1 = Work.objects.filter().all()
    print(Work1)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-view-work.html' , {'work_deatil' : Work1 , 'info':info})

def edit_work(request,edit_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    adminid = request.session['adminid']
    info2 = admin1.objects.filter(id=adminid).get()
    all_work_cat = Workcategory.objects.all()
    info=Work.objects.filter(id=edit_id).get()
    obj=Workform(instance=info)
    msg=""
    if 'save' in request.POST:
        obj=Workform(request.POST,request.FILES,instance=info)
        if obj.is_valid():
            obj.save()
            msg="data update"
            return redirect("/viewwork/")
        print(info)
    return render(request,'admin-add-work.html',{'Work':info,'msg':msg,'all_work_cat':all_work_cat,'info2':info2})

def delete_work_view(request,del_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    Work.objects.get(id=del_id).delete()
    return redirect('/viewwork/')

# --------------------------------------------------------------------------- Clients ------------

def adminclients(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    msg=""
    obj = Clientsform()
    if 'save' in request.POST:
        obj = Clientsform(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
            msg = "Success"
            return redirect('/viewclients/')
    adminid = request.session['adminid']
    info = admin1.objects.filter(id = adminid).get()
    return render(request,'admin-add-clients.html',{'msg':msg,'info':info})


def view_clients(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    clients1 = Clients.objects.filter().all()
    print(clients1)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-view-clients.html' , {'clients_deatil' : clients1 , 'info':info})

def edit_clients(request,edit_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    adminid = request.session['adminid']
    info2 = admin1.objects.filter(id=adminid).get()
    info=Clients.objects.filter(id=edit_id).get()
    obj=Clientsform(instance=info)
    msg=""
    if 'save' in request.POST:
        obj=Clientsform(request.POST,request.FILES,instance=info)
        if obj.is_valid():
            obj.save()
            msg="data update"
            return redirect("/viewclients/")
        print(info)
    return render(request,'admin-add-clients.html',{'clients':info,'msg':msg,'info2':info2})

def delete_clients_view(request,del_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    Clients.objects.get(id=del_id).delete()
    return redirect('/viewclients/')

def ajax_search_blog(request):
    searchkeyword = request.GET['search_blog']
    data = blog.objects.filter(Tital__contains=searchkeyword).all()
    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td>'+row.Tital+'</td><td>'+row.Description+'</td><td>'+str(row.Cat_id)+'</td><td>'+str(row.Admin_id)+'</td><td><img src="../../media/'+row.Picture.url+'" alt="" width="70px" height="70px" style="object-fit: cover; border-radius: 20px;"></td><td><a href="/editblog/'+str(row.id)+'"><button type="button" class="btn btn-outline-primary">Edit Profile</button></a><a href="/deleteblog/'+str(row.id)+'""><button type="button" class="btn btn-outline-danger">Delete</button></a></td></tr>'
    return HttpResponse(htmlData)

def ajax_search_work(request):
    searchkeyword = request.GET['search_work']
    data = Work.objects.filter(Name__contains=searchkeyword).all()
    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td>'+row.Name+'</td><td>'+row.Description+'</td><td>'+str(row.Work_Category)+'</td><td><img src="../../media/'+row.Picture.url+'" alt="" width="70px" height="70px" style="object-fit: cover; border-radius: 20px;"></td><td><a href="/editwork/'+str(row.id)+'"><button type="button" class="btn btn-outline-primary">Edit Profile</button></a><a href="/deletework/'+str(row.id)+'""><button type="button" class="btn btn-outline-danger">Delete</button></a></td></tr>'
    return HttpResponse(htmlData)

def ajax_search_admin(request):
    searchkeyword = request.GET['search_admin']
    data = admin1.objects.filter(Name__contains=searchkeyword).all()
    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td>'+row.Name+'</td><td>'+row.Email+'</td><td>'+str(row.Password)+'</td><td>'+str(row.Contact)+'</td><td><img src="../../media/'+row.Picture.url+'" alt="" width="70px" height="70px" style="object-fit: cover; border-radius: 20px;"></td><td><a href="/editprofile/'+str(row.id)+'"><button type="button" class="btn btn-outline-primary">Edit Profile</button></a><a href="/deleteadmin/'+str(row.id)+'""><button type="button" class="btn btn-outline-danger">Delete</button></a></td></tr>'
    return HttpResponse(htmlData)

def ajax_search_slider(request):
    searchkeyword = request.GET['search_slider']
    data = slider.objects.filter(Tital__contains=searchkeyword).all()
    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td>'+row.Tital+'</td><td>'+row.Description+'</td><td><img src="../../media/'+row.Picture.url+'" alt="" width="70px" height="70px" style="object-fit: cover; border-radius: 20px;"></td><td><a href="/editslider/'+str(row.id)+'"><button type="button" class="btn btn-outline-primary">Edit Profile</button></a><a href="/deleteslider/'+str(row.id)+'""><button type="button" class="btn btn-outline-danger">Delete</button></a></td></tr>'
    return HttpResponse(htmlData)

def ajax_search_service(request):
    searchkeyword = request.GET['search_services']
    data = services.objects.filter(Tital__contains=searchkeyword).all()
    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td>'+row.Icon+'</td><td>'+row.Tital+'</td><td>'+row.Description+'</td><td><a href="/editservices/'+str(row.id)+'"><button type="button" class="btn btn-outline-primary">Edit Profile</button></a><a href="/deleteservices/'+str(row.id)+'""><button type="button" class="btn btn-outline-danger">Delete</button></a></td></tr>'
    return HttpResponse(htmlData)

def ajax_search_blogcategory(request):
    searchkeyword = request.GET['search_blogcategory']
    data = blogcategory.objects.filter(Name__contains=searchkeyword).all()
    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td>'+row.Name+'</td><td><a href="/editblogcatrgory/'+str(row.id)+'"><button type="button" class="btn btn-outline-primary">Edit Profile</button></a><a href="/deleteblogcategory/'+str(row.id)+'""><button type="button" class="btn btn-outline-danger">Delete</button></a></td></tr>'
    return HttpResponse(htmlData)

def ajax_search_workcategory(request):
    searchkeyword = request.GET['search_workcategory']
    data = Workcategory.objects.filter(Name__contains=searchkeyword).all()
    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td>'+row.Name+'</td><td><a href="/editworkcatrgory/'+str(row.id)+'"><button type="button" class="btn btn-outline-primary">Edit Profile</button></a><a href="/deleteworkcategory/'+str(row.id)+'""><button type="button" class="btn btn-outline-danger">Delete</button></a></td></tr>'
    return HttpResponse(htmlData)

def ajax_search_clients(request):
    searchkeyword = request.GET['search_clients']
    data = Clients.objects.filter(Name__contains=searchkeyword).all()
    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td><img src="../../media/'+row.Picture.url+'" alt="" width="70px" height="70px" style="object-fit: cover; border-radius: 20px;"></td><td>'+row.Name+'</td><td>'+row.Link+'</td><td><a href="/editclients/'+str(row.id)+'"><button type="button" class="btn btn-outline-primary">Edit Profile</button></a><a href="/deleteclients/'+str(row.id)+'""><button type="button" class="btn btn-outline-danger">Delete</button></a></td></tr>'
    return HttpResponse(htmlData)

def ajax_search_comments(request):
    searchkeyword = request.GET['search_comments']
    data = comments.objects.filter(Name__contains=searchkeyword).all()
    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td><img src="../../media/'+row.Picture.url+'" alt="" width="70px" height="70px" style="object-fit: cover; border-radius: 20px;"></td><td>'+row.Name+'</td><td>'+row.Subject+'</td><td>'+row.Comment+'</td><td>'+str(row.Blogid_id)+'</td></tr>'
    return HttpResponse(htmlData)

def ajax_search_contact(request):
    searchkeyword = request.GET['search_contact']
    data = Contact.objects.filter(Name__contains=searchkeyword).all()
    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td>'+row.Name+'</td><td>'+row.Email+'</td><td>'+row.Subject+'</td><td>'+row.Message+'</td></tr>'
    return HttpResponse(htmlData)