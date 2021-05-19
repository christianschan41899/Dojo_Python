from django.shortcuts import render, redirect
from django.contrib import messages
from .models import tvShow

def root(request):
    return redirect('/shows')

def tvShowList(request):
    context = {
        'all_shows' : tvShow.objects.all()
    }
    return render(request, 'displayShowList.html', context)

def newShow(request):
    return render(request, 'addShow.html')

def createShow(request):
    errors = tvShow.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        tvShow.objects.create(title = request.POST['title'], network = request.POST['network'], release_date = request.POST['release_date'], desc = request.POST['desc'])
        #When a tvShow is created it should be in the last row of the table, so .last() would access it.
        submitted_show = tvShow.objects.last()
        return redirect('/shows/'+ str(submitted_show.id))

def tvShowDisplay(request, show_id):
    context = {
        'current_show' : tvShow.objects.get(id = show_id)
    }
    return render(request, 'displayShow.html', context)

def tvShowEditForm(request, show_id):
    context = {
        'editing_show' : tvShow.objects.get(id = show_id)
    }
    return render(request, 'editShow.html', context)

def tvShowUpdate(request, show_id):
    errors = tvShow.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+ str(show_id) + '/edit')
    else:
        edit_show = tvShow.objects.get(id = show_id)
        edit_show.title = request.POST['title']
        edit_show.network = request.POST['network']
        edit_show.release_date = request.POST['release_date']
        edit_show.desc = request.POST['desc']
        edit_show.save()
        return redirect('/shows/' + str(edit_show.id))

def tvShowDestroy(request, show_id):
    delete_show = tvShow.objects.get(id = show_id)
    delete_show.delete()
    return redirect('/')
# Create your views here.
