from django.db import models
from django.contrib.auth.models import User


class ResumeBuilder(models.Model):
    first_name = models.CharField(max_length=500, null=True, blank=True)
    last_name = models.CharField(max_length=500, null=True, blank=True)
    jobtitle = models.CharField(max_length=500, null=True, blank=True)
    aboutme = models.TextField(null=True, blank=True)
    email = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=500, null=True, blank=True)
    github = models.CharField(max_length=500, null=True, blank=True)
    linkedin = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(
        upload_to="Resume Image", default='default.png')
    positiontitle1 = models.CharField(max_length=500, null=True, blank=True)
    employer = models.CharField(max_length=500, null=True, blank=True)
    positioncity = models.CharField(max_length=500, null=True, blank=True)
    positionyear = models.CharField(max_length=500, null=True, blank=True)
    positionmonth = models.CharField(max_length=500, null=True, blank=True)
    todayyear = models.CharField(max_length=500, null=True, blank=True)
    todaymonth = models.CharField(max_length=500, null=True, blank=True)
    todayfdsaf = models.CharField(max_length=500, null=True, blank=True)
    degreefield = models.CharField(max_length=500, null=True, blank=True)
    degree = models.CharField(max_length=500, null=True, blank=True)
    degreeschoolname = models.CharField(max_length=500, null=True, blank=True)
    degreeschoolcity = models.CharField(max_length=500, null=True, blank=True)
    degreeschoolyear = models.CharField(max_length=500, null=True, blank=True)
    degreeschoolmonth = models.CharField(max_length=500, null=True, blank=True)
    degreeschooltoyear = models.CharField(
        max_length=500, null=True, blank=True)
    degreeschooltomonth = models.CharField(
        max_length=500, null=True, blank=True)
    hscfield = models.CharField(max_length=500, null=True, blank=True)
    hscdegree = models.CharField(max_length=500, null=True, blank=True)
    hscdegreeschoolname = models.CharField(
        max_length=500, null=True, blank=True)
    hscdegreeschoolcity = models.CharField(
        max_length=500, null=True, blank=True)
    hscdegreeschoolyear = models.CharField(
        max_length=500, null=True, blank=True)
    hscdegreeschoolmonth = models.CharField(
        max_length=500, null=True, blank=True)
    hscdegreeschooltoyear = models.CharField(
        max_length=500, null=True, blank=True)
    hscdegreeschooltomonth = models.CharField(
        max_length=500, null=True, blank=True)
    skills = models.CharField(max_length=500, null=True, blank=True)
    footer = models.CharField(max_length=500, null=True, blank=True)
    hobby = models.CharField(max_length=500, null=True, blank=True)
    language = models.CharField(max_length=500, null=True, blank=True)
    certificate = models.CharField(max_length=500, null=True, blank=True)
    certificateyear = models.CharField(max_length=500, null=True, blank=True)
    certificatemonth = models.CharField(max_length=500, null=True, blank=True)
    certificate1 = models.CharField(max_length=500, null=True, blank=True)
    certificateyear1 = models.CharField(max_length=500, null=True, blank=True)
    certificatemonth1 = models.CharField(max_length=500, null=True, blank=True)
    certificate2 = models.CharField(max_length=500, null=True, blank=True)
    certificateyear2 = models.CharField(max_length=500, null=True, blank=True)
    certificatemonth2 = models.CharField(max_length=500, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
