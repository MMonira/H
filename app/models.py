from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
   USER_TYPES = [
        ('candidate', 'Candidate'),
        ('employer', 'Employer')
    ]
   GENDERS = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]

   user_type = models.CharField(max_length=50, choices=USER_TYPES , null= True)
   gender = models.CharField(max_length=50, choices=GENDERS , null= True)
   profile_picture = models.ImageField(upload_to='static/profile_pictures/', null=True)

   def __str__(self):
      return f"{self.username or ''} {self.user_type or ''}"
 
 
JOB_TYPE_CHOICES = [
    ('freelance', 'Freelance'),
    ('full_time', 'Full Time'),
    ('internship', 'Internship'),
    ('part_time', 'Part Time'),
    ('spot_time', 'Spot Time'),
]

GENDER_TYPE =[
    ('any','Any'),
    ('Male','Male'),
    ('Female','Female'),
]

TYPE =[
  
    ('Male','Male'),
    ('Female','Female'),
    ('other','other'),
]

SALARY_TYPE_CHOICES = [
    ('hourly', 'Hourly'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('yearly', 'Yearly'),
    ('project_base', 'Project Base'),
]

CURRENCY_TYPE_CHOICES = [
    ('dollar', 'Dollar'),
    ('taka', 'Taka'),
]

ACADEMIC_QUALIFICATION_CHOICES = [
    ('PSC', 'Primary School Certificate (PSC)'),
    ('JSC', 'Junior School Certificate (JSC)'),
    ('SSC', 'Secondary School Certificate (SSC)'),
    ('HSC', 'Higher Secondary Certificate (HSC)'),
    ('Honours', 'Honours'),
    ('Masters', "Master's"),
    ('Phd', 'PhD'),
]
 
 
 
class Candidate(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True)
    
    years_of_experience = models.IntegerField(null=True)
    #AcademicQualification
    
    institute_name = models.CharField(max_length=255,null=True)
    degree_name = models.CharField(max_length=100,null=True)
    grade = models.CharField(max_length=50,null=True)

    resume_file = models.FileField(upload_to='resumes/', null=True, blank=True)
    
    
    #work experei
    
    
    organization_name = models.CharField(max_length=255,null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True, blank=True)
    currently_working_here = models.BooleanField(default=False)
    job_description = models.TextField(null=True)
    
    
    Mobile = models.CharField(max_length=50, null=True)
    EmergencyContact = models.CharField(max_length=50, null=True)
    PresentAddress = models.CharField(max_length=100, null=True)
    PermanentAddress = models.CharField(max_length=100, null=True)

    def __str__(self):
       return f"{self.user.username} {self.years_of_experience or ''}"

  
class CompanyProfile(models.Model):
    employer = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    company_name = models.CharField(max_length=255,null=True)
    website = models.URLField(null=True)
    headline = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    full_address = models.TextField(null=True)
    phone = models.CharField(max_length=20,null=True)
    description = models.TextField(null=True)
    
    
    def __str__(self):
        return f"{self.employer.username} {self.company_name or ''}"

class JobInfo(models.Model):
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    job_title = models.CharField(max_length=255,null=True)
    industry = models.CharField(max_length=100,null=True)
    department = models.CharField(max_length=100,null=True)
    position = models.CharField(max_length=100,null=True)
    application_deadline = models.DateField(null=True)
    specific_gender = models.CharField(choices= GENDER_TYPE , max_length=10, null=True, blank=True) 
    job_description = models.TextField(null=True)
    job_requirements = models.TextField(null=True)
    academic_qualifications = models.CharField(max_length=20, choices=ACADEMIC_QUALIFICATION_CHOICES,null=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES,null=True)
    salary_type = models.CharField(max_length=20, choices=SALARY_TYPE_CHOICES,null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    experience = models.IntegerField(null=True)
    job_skills = models.TextField(null=True)
    number_of_vacancies = models.IntegerField(null=True)
    posted_date = models.DateField(auto_now_add=True,null=True,blank=True)
    company_logo = models.ImageField(upload_to='job_images/', null=True, blank=True)
  

    def __str__(self):
        return f"{self.job_title or ''} {self.job_type or ''}"
    
class Applicant(models.Model):
    apply_to = models.ForeignKey(JobInfo, on_delete=models.CASCADE, null=True)
    apply_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='applicantinfo', null=True)
    skills=models.CharField(max_length=100,null=True)
    resume = models.FileField(upload_to='resumes/', null=True)
    profileimage= models.ImageField(upload_to='media/seeker_img',null=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('reviewed', 'Reviewed'), ('accepted', 'Accepted'), ('rejected', 'Rejected')] , default= 'pending')
    applied_at = models.DateTimeField(auto_now_add=True)