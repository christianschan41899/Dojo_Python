from django.db import models


#These will be pre-populated in the 
class Equip(models.Model):
    name = models.TextField()
    dmgType = models.TextField()
    slotSpace = models.IntegerField()
    tons = models.DecimalField(max_digits = 3, decimal_places = 1)


#Chassis for disply in the hangar
class displayChassis(models.Model):
    name = models.TextField()
    tons = models.IntegerField()
    tot_eSlots = models.IntegerField(default = 0)
    tot_bSlots = models.IntegerField(default = 0)
    tot_mSlots = models.IntegerField(default = 0)
    tot_oSlots = models.IntegerField(default = 0)
    hangar_src = models.TextField()
    mechlab_src = models.TextField()

#Template parts used to store mech slot numbers.
class templatePart(models.Model):
    name = models.TextField()
    #Slots and their type for each slot
    eSlots = models.IntegerField(default = 0)
    bSlots = models.IntegerField(default = 0)
    mSlots = models.IntegerField(default = 0)
    oSlots = models.IntegerField(default = 0)
    #Assigned Mech
    displayedMech = models.ForeignKey(displayChassis, related_name = "displayedParts", on_delete = models.CASCADE)

#Mech Chassis for editing. This will hold the parts we want.
class Chassis(displayChassis):
    tons_armor = models.DecimalField(max_digits = 3, decimal_places = 1)
    tons_engine = models.DecimalField(max_digits = 3, decimal_places = 1)
    
#Mech parts editable by the user. Left and Right Arm, Left and Right Torso, and Center Torso
class Part(models.Model):
    #equipment
    name = models.TextField()
    #Slots and their type for each slot
    eSlots = models.IntegerField(default = 0)
    bSlots = models.IntegerField(default = 0)
    mSlots = models.IntegerField(default = 0)
    oSlots = models.IntegerField(default = 0)
    #Assigned Mech
    mech = models.ForeignKey(Chassis, related_name = "parts", on_delete = models.CASCADE)
#    equipped = models.ManyToManyField(Equip, related_name = "assign_part")
    



