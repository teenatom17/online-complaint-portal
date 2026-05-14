from django.contrib import admin
from .models import Complaint
from .models import ContactMessage

admin.site.register(Complaint)
#from .models import (
    #Citizen,
    #PoliceStation,
    #PoliceOfficer,
    #FIR,
    #Investigation,
    #Charges,
    #Evidence,
    #Complaint,
    #ContactMessage
#)

#admin.site.register(Citizen)
#admin.site.register(PoliceStation)
#admin.site.register(PoliceOfficer)
#admin.site.register(FIR)
#admin.site.register(Investigation)
#admin.site.register(Charges)
#admin.site.register(Evidence)
#admin.site.register(Complaint)
admin.site.register(ContactMessage)


