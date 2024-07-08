from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import *
from django.db.models import Q
from .forms import *
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from notifications.signals import notify


def signuppage(request):
   if request.method == "POST":
      username = request.POST.get('username')
      email = request.POST.get('email')
      gender = request.POST.get('gender')
      user_type = request.POST.get('user_type')
      profile_photo = request.FILES.get('profile_photo')
      password = request.POST.get('password')
      confirm_password = request.POST.get('confirm_password')

      if password == confirm_password :
         user = CustomUser.objects.create_user (
            username = username,
            email = email ,
            gender = gender,
            user_type = user_type ,
            profile_picture = profile_photo ,
            password = password,
         )

         user.save()
         return  redirect('signin')
      else:
         return redirect('signup')


   return render(request,'signuppage.html')


def signin(request):
   if request.method == "POST":
      username = request.POST.get('username')
      password = request.POST.get('password')

      user = authenticate(username = username, password = password)

      if user is not None :
         login(request, user)
         return redirect('dashboard')
      else:
         messages.error(request, 'Invalid username or password')

   return render(request,'signin.html')


def searchpage(request):
   if request.method == 'GET':
      query = request.GET.get('search')

      search = JobInfo.objects.filter(
         Q(job_title__icontains =  query) |
         Q (industry__icontains = query) |
         Q (salary__icontains = query)
      )
      
      job_filtered = []

      for job in search:
         already_applied = Applicant.objects.filter(apply_by = request.user, apply_to = job).exists()
         
         job_filtered.append((job, already_applied),)
      
      context = {
         'query':query,
         'search':search,
         'job_filtered':job_filtered,
      }
   return render(request,'searchpage.html', context)

@login_required

def applyjob(request , myid):
   job = get_object_or_404(JobInfo, id = myid)

   if request.method == 'POST':
      skills = request.POST.get('skills')
      resume = request.FILES.get('resume')
      cover_letter = request.POST.get('cover_letter')

      application = Applicant.objects.create(
         apply_by = request.user,
         apply_to = job,
         skills = skills,
         resume = resume,
         cover_letter = cover_letter,
      )
      application.save()
      return redirect('viewjob')

   return render(request,'applyjob.html')


@login_required
def viewjob(request):
   jobs = JobInfo.objects.all()
   job_filtered = []

   for job in jobs:
      already_applied = Applicant.objects.filter(apply_by = request.user, apply_to = job).exists()
      
      job_filtered.append((job, already_applied),)
      
      
   return render(request,'viewjob.html',{'jobs':jobs,'job_filtered': job_filtered})





@login_required
def postjob(request):
   if request.method == 'POST':
      jobForm = jobinfoForm(request.POST , request.FILES)
      if jobForm.is_valid():
         j = jobForm.save(commit=False)
         j.created_by = request.user
         j.save()
         notify.send(sender=request.user , recipient = request.user , verb='You posted a job' , action_object=j)
         return redirect('viewjob')
   else:
      jobForm = jobinfoForm()
   return render(request,'postjob.html',{'jobform':jobForm})



@login_required
def appliedjob(request):
   jobs = Applicant.objects.filter(apply_by = request.user)

   return render(request,'appliedjob.html',{'jobs':jobs})


@login_required
def logoutpage(request):
   logout(request)
   return redirect('signin')

@login_required
def profile(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)


@login_required
def changePassword(request):
   if request.method == "POST":
      cpassword = request.POST.get('cpassword')
      password = request.POST.get('password')
      confirmPassword = request.POST.get('confirmPassword')
      
      if check_password(cpassword , request.user.password):
         if password == confirmPassword :
            request.user.set_password(password)
            request.user.save()
            update_session_auth_hash(request,request.user)
            return redirect('profile')

   return render(request,'changePassword.html')
   
   
def navbar(request):
   return render(request,'navbar.html')
   
@login_required
def notificationspage(request):
    
    notifications = request.user.notifications.all()
    notification_count = notifications.count()
    
    context = {
        'notifications': notifications,
        'notification_count': notification_count
    }
    return render(request, 'notificationspage.html', context)


@login_required
def editprofile(request):
   return render(request,'editprofile.html')
   