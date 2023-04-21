from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


def homepage(request):
    context = {
        'username': request.user
    }
    return render(request, "builderpage/homepage.html", context)


def builder(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            jobtitle = request.POST.get('jobtitle')
            aboutme = request.POST.get('aboutme')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            github = request.POST.get('github')
            linkedin = request.POST.get('Linkedin')
            image = request.FILES.get('image')
            positiontitle1 = request.POST.get('positiontitle1')
            employer = request.POST.get('employer')
            positioncity = request.POST.get('positioncity')
            positionyear = request.POST.get('positionyear')
            positionmonth = request.POST.get('positionmonth')
            todayyear = request.POST.get('todayyear')
            todaymonth = request.POST.get('todaymonth')
            todayfdsaf = request.POST.get('todayfdsaf')
            degreefield = request.POST.get('degreefield')
            degree = request.POST.get('degree')
            degreeschoolname = request.POST.get('degreeschoolname')
            degreeschoolcity = request.POST.get('degreeschoolcity')
            degreeschoolyear = request.POST.get('degreeschoolyear')
            degreeschoolmonth = request.POST.get('degreeschoolmonth')
            degreeschooltoyear = request.POST.get('degreeschooltoyear')
            degreeschooltomonth = request.POST.get('degreeschooltomonth')
            hscfield = request.POST.get('hscfield')
            hscdegree = request.POST.get('hscdegree')
            hscdegreeschoolname = request.POST.get('hscdegreeschoolname')
            hscdegreeschoolcity = request.POST.get('hscdegreeschoolcity')
            hscdegreeschoolyear = request.POST.get('hscdegreeschoolyear')
            hscdegreeschoolmonth = request.POST.get('hscdegreeschoolmonth')
            hscdegreeschooltoyear = request.POST.get('hscdegreeschooltoyear')
            hscdegreeschooltomonth = request.POST.get('hscdegreeschooltomonth')
            skills = request.POST.get('skills')
            footer = request.POST.get('footer')
            hobby = request.POST.get('hobby')
            language = request.POST.get('language')
            certificate = request.POST.get('certificate')
            certificateyear = request.POST.get('certificateyear')
            certificatemonth = request.POST.get('certificatemonth')
            certificate1 = request.POST.get('certificate1')
            certificateyear1 = request.POST.get('certificateyear1')
            certificatemonth1 = request.POST.get('certificatemonth1')
            certificate2 = request.POST.get('certificate2')
            certificateyear2 = request.POST.get('certificateyear2')
            certificatemonth2 = request.POST.get('certificatemonth2')

            ResumeBuilder(first_name=first_name, last_name=last_name, jobtitle=jobtitle, aboutme=aboutme, email=email, phone=phone, github=github, linkedin=linkedin, image=image, positiontitle1=positiontitle1, employer=employer, positioncity=positioncity, positionyear=positionyear, positionmonth=positionmonth, todayyear=todayyear, todaymonth=todaymonth, todayfdsaf=todayfdsaf, degreefield=degreefield, degree=degree, degreeschoolname=degreeschoolname, degreeschoolcity=degreeschoolcity, degreeschoolyear=degreeschoolyear, degreeschoolmonth=degreeschoolmonth, degreeschooltoyear=degreeschooltoyear, degreeschooltomonth=degreeschooltomonth, hscfield=hscfield, hscdegree=hscdegree,
                          hscdegreeschoolname=hscdegreeschoolname, hscdegreeschoolcity=hscdegreeschoolcity,
                          hscdegreeschoolyear=hscdegreeschoolyear, hscdegreeschoolmonth=hscdegreeschoolmonth, hscdegreeschooltoyear=hscdegreeschooltoyear, hscdegreeschooltomonth=hscdegreeschooltomonth, skills=skills, footer=footer, hobby=hobby, language=language, certificate=certificate, certificateyear=certificateyear, certificatemonth=certificatemonth, certificate1=certificate1, certificateyear1=certificateyear1, certificatemonth1=certificatemonth1, certificate2=certificate2, certificateyear2=certificateyear2, certificatemonth2=certificatemonth2, user=request.user).save()

            return redirect('download_resume')
        context = {
            'username': request.user,
        }
        return render(request, "builderpage/index.html", context)
    else:
        return redirect('login')


def updateResume(request, id):
    obj = ResumeBuilder.objects.get(id=id)
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        jobtitle = request.POST.get('jobtitle')
        aboutme = request.POST.get('aboutme')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        github = request.POST.get('github')
        linkedin = request.POST.get('Linkedin')
        image = request.FILES.get('image')
        positiontitle1 = request.POST.get('positiontitle1')
        employer = request.POST.get('employer')
        positioncity = request.POST.get('positioncity')
        positionyear = request.POST.get('positionyear')
        positionmonth = request.POST.get('positionmonth')
        todayyear = request.POST.get('todayyear')
        todaymonth = request.POST.get('todaymonth')
        todayfdsaf = request.POST.get('todayfdsaf')
        degreefield = request.POST.get('degreefield')
        degree = request.POST.get('degree')
        degreeschoolname = request.POST.get('degreeschoolname')
        degreeschoolcity = request.POST.get('degreeschoolcity')
        degreeschoolyear = request.POST.get('degreeschoolyear')
        degreeschoolmonth = request.POST.get('degreeschoolmonth')
        degreeschooltoyear = request.POST.get('degreeschooltoyear')
        degreeschooltomonth = request.POST.get('degreeschooltomonth')
        hscfield = request.POST.get('hscfield')
        hscdegree = request.POST.get('hscdegree')
        hscdegreeschoolname = request.POST.get('hscdegreeschoolname')
        hscdegreeschoolcity = request.POST.get('hscdegreeschoolcity')
        hscdegreeschoolyear = request.POST.get('hscdegreeschoolyear')
        hscdegreeschoolmonth = request.POST.get('hscdegreeschoolmonth')
        hscdegreeschooltoyear = request.POST.get('hscdegreeschooltoyear')
        hscdegreeschooltomonth = request.POST.get('hscdegreeschooltomonth')
        skills = request.POST.get('skills')
        footer = request.POST.get('footer')
        hobby = request.POST.get('hobby')
        language = request.POST.get('language')
        certificate = request.POST.get('certificate')
        certificateyear = request.POST.get('certificateyear')
        certificatemonth = request.POST.get('certificatemonth')
        certificate1 = request.POST.get('certificate1')
        certificateyear1 = request.POST.get('certificateyear1')
        certificatemonth1 = request.POST.get('certificatemonth1')
        certificate2 = request.POST.get('certificate2')
        certificateyear2 = request.POST.get('certificateyear2')
        certificatemonth2 = request.POST.get('certificatemonth2')

        picture = None
        if image == None:
            picture = obj.image
        else:
            picture = image

        ResumeBuilder(id=id, first_name=first_name, last_name=last_name, jobtitle=jobtitle, aboutme=aboutme, email=email, phone=phone, github=github, linkedin=linkedin, image=picture, positiontitle1=positiontitle1, employer=employer, positioncity=positioncity, positionyear=positionyear, positionmonth=positionmonth, todayyear=todayyear, todaymonth=todaymonth, todayfdsaf=todayfdsaf, degreefield=degreefield, degree=degree, degreeschoolname=degreeschoolname, degreeschoolcity=degreeschoolcity, degreeschoolyear=degreeschoolyear, degreeschoolmonth=degreeschoolmonth, degreeschooltoyear=degreeschooltoyear, degreeschooltomonth=degreeschooltomonth, hscfield=hscfield,
                      hscdegree=hscdegree, hscdegreeschoolname=hscdegreeschoolname, hscdegreeschoolcity=hscdegreeschoolcity, hscdegreeschoolyear=hscdegreeschoolyear, hscdegreeschoolmonth=hscdegreeschoolmonth, hscdegreeschooltoyear=hscdegreeschooltoyear, hscdegreeschooltomonth=hscdegreeschooltomonth, skills=skills, footer=footer, hobby=hobby, language=language, certificate=certificate, certificateyear=certificateyear, certificatemonth=certificatemonth, certificate1=certificate1, certificateyear1=certificateyear1, certificatemonth1=certificatemonth1, certificate2=certificate2, certificateyear2=certificateyear2, certificatemonth2=certificatemonth2, user=request.user).save()

        return redirect('download_resume')

    context = {
        'username': request.user,
        'resume': obj
    }
    return render(request, "builderpage/updateresume.html", context)


def download_resume(request):
    obj = ResumeBuilder.objects.filter(user=request.user).last()
    if obj:
        skills = obj.skills.split(",")
        language = obj.language.split(",")
        hobby = obj.hobby.split(",")
        return render(request, "builderpage/download.html", locals())
    return redirect('builder')
