from django.urls import path
from .views import *

urlpatterns = [
   path('',signin , name='signin'),
   path('signup/',signuppage , name='signup'),
   
   path('searchpage/',searchpage , name='searchpage'),
   path('viewjob/',viewjob , name='viewjob'),
   path('postjob/',postjob , name='postjob'),
   path('appliedjob/',appliedjob , name='appliedjob'),
   path('logoutpage/',logoutpage , name='logoutpage'),
   path('profile/',profile , name='profile'),
   path('changePassword/',changePassword , name='changePassword'),
   path('navbar/',navbar , name='navbar'),
   path('editprofile/',editprofile , name='editprofile'),
   path('notificationspage/',notificationspage , name='notificationspage'),
   path('applyjob/<int:myid>',applyjob , name='applyjob'),
]
