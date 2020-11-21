from django.urls import path
from .views import home,career,blog,services


urlpatterns = [	
	path('services/',services,name='services_url'),
	path('career/',career,name='career_url'),
	path('blog/',blog,name='blog_url'),
    path('',home,name='home_url')
]