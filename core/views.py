from core.models import Comment, CommentForm
from itertools import ifilter
import json
from core.reg_forms import *
from core.taskform import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from core.models import Image
from core.forms import DocumentForm
from django.db.models import Q


def auth_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/list')
    return HttpResponseRedirect(request.path_info+'?auth_error=true')


def user_logout(request):
    if request.method == 'GET':
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseBadRequest()
    return HttpResponseBadRequest('Not Allowed')
 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
def register_success(request):
    return render_to_response(
    'registration/success.html',
)

@login_required
def home(request,pid):
    form = CommentForm(request.POST or None)
    user = User.objects.filter(id=request.user.id)
    image = Image.objects.filter(id=pid)[0]
    print image.status,request.user.id,image.user.id
    if image.status=='Only Me' and image.user!=request.user:
        return HttpResponse('Unauthorized', status=401) 
    else:
        if request.method == "POST":
            if form.is_valid():
                print type(form)
                temp = form.save(commit=False)
                print type(temp)
                parent = form['parent'].value()
                
                if parent == '':
                    #Set a blank path then save it to get an ID
                    temp.path = []
                    temp.save()
                    temp.path = [temp.id]
                else:
                    #Get the parent node
                    node = Comment.objects.get(id=parent)
                    temp.depth = node.depth + 1
                    temp.path = node.path
                    
                    #Store parents path then apply comment ID
                    temp.save()
                    temp.path.append(temp.id)
                    
                #Final save for parents and children
                temp.image = image
                temp.user= request.user
                temp.save()
                return redirect('/list/home/image/'+pid+'/') 

        # Retrieve all comments and sort them by path
        comment_tree = Comment.objects.filter(image=image).order_by('path')          
        return render(request, 'index.html',{"image":image,"form":form,
                      "comment_tree":comment_tree })
           

@login_required
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newimage = Image(imagefile = request.FILES['docfile'],user=request.user,status=request.POST['select'])
            newimage.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect('/list')
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    images = Image.objects.filter(user=request.user)

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'images': images, 'form': form},
        context_instance=RequestContext(request)
    )

@login_required
def list_community_image(request):
    # Handle file upload
    images = Image.objects.filter(Q(status='Community')| Q(status='Public'))

    # Render list page with the documents and the form
    return render_to_response(
        'shared_images.html',
        {'images': images},
        context_instance=RequestContext(request)
    )    

def landing_page(request):
    # Handle file upload
    images = Image.objects.filter(status='Public')

    # Render list page with the documents and the form
    return render_to_response(
        'landing_page.html',
        {'images': images},
        context_instance=RequestContext(request)
    )       