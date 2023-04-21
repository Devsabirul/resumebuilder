from django.urls import path
from .views import *
urlpatterns = [
    path('', homepage, name="homepage"),
    path('builder', builder, name="builder"),
    path('updateResume/<int:id>', updateResume, name="updateResume"),
    path('builder/download', download_resume, name="download_resume"),
]
