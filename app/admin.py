from django.contrib import admin
from .models import *


admin.site.register(CustomUser)

admin.site.register(JobInfo)
admin.site.register(Candidate)
admin.site.register(CompanyProfile)
admin.site.register(Applicant)
