from django.shortcuts import render, redirect

def root(request):
    return render(request,'form.html')

def survey(request):
    form_fullname = request.POST["full_name"]
    form_location = request.POST["locations"]
    form_favlang = request.POST["fav_lang"]
    form_comment = request.POST["comment"]
    context = {
        "fullname" : form_fullname,
        "location" : form_location,
        "favlang" : form_favlang,
        "comment" : form_comment
    }
    return render(request, 'results.html', context)

# Create your views here.
