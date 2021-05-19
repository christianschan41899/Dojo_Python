from django.shortcuts import render, redirect
from .models import displayChassis, Chassis, Part, Equip

# Create your views here.
def hangar(request):
    context = {
        "lights" : displayChassis.objects.filter(tons__range=(20, 35)),
        "mediums" : displayChassis.objects.filter(tons__range=(40, 55)),
        "heavies" : displayChassis.objects.filter(tons__range=(60, 70)),
        "assaults" : displayChassis.objects.filter(tons__range=(80, 100))
    }

    return render(request, "hangar.html", context)

def create(request):
    base_chassis = displayChassis.objects.get(id = request.POST['mech_id'])
    editing_chassis = Chassis.objects.create(
        name = base_chassis.name,
        tons = base_chassis.tons,
        tot_eSlots = base_chassis.tot_eSlots,
        tot_mSlots = base_chassis.tot_mSlots,
        tot_bSlots = base_chassis.tot_bSlots,
        tot_oSlots = base_chassis.tot_oSlots,
        hangar_src = base_chassis.hangar_src,
        mechlab_src = base_chassis.hangar_src,
        tons_armor = 0.0,
        tons_engine = 0.0
    )
    request.session['currentMech'] = editing_chassis
    return redirect('/mechlab')

def mechLab(request):
    context = {
        'chassis' : request.session['currentMech']
    }
    render(request, "mechLab.html", context)
