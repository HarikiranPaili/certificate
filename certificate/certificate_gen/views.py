from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import *
from .resources import PersonResource
from tablib import Dataset
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import openpyxl
# Create your views here.

#@login_required(login_url='login')
def add_event(request):
    if request.method == 'POST':
        # adding event
        event_name = request.POST.get('event_name')
        event_start_date = request.POST.get('event_start_date')
        event_end_date = request.POST.get('event_end_date')
        organizer = request.POST.get('organizer')
        if organizer:
            organizer_name = organizer
        else:
            organizer_name = 'None'
        create_event = Event_details.objects.create(event_name=event_name,event_start_date=event_start_date,
                                                    event_end_date=event_end_date,organizer=organizer_name)
        create_event.save()

        # adding signs
        Signatories_name_1 = request.POST.get('Signatories_name_1')
        digital_Signatures_1 = request.POST.get('digital_Signatures_1')
        create_sign_1 = Signs.objects.create(Signatories_name=Signatories_name_1, digital_Signatures=digital_Signatures_1,
                                           event_name=event_name)
        create_sign_1.save()
        Signatories_name_2 = request.POST.get('Signatories_name_2')
        digital_Signatures_2 = request.POST.get('digital_Signatures_2')
        create_sign_2 = Signs.objects.create(Signatories_name=Signatories_name_2, digital_Signatures=digital_Signatures_2,
                                           event_name=event_name)
        create_sign_2.save()
        Signatories_name_3 = request.POST.get('Signatories_name_3')
        digital_Signatures_3 = request.POST.get('digital_Signatures_3')
        if Signatories_name_3 and digital_Signatures_3:
            create_sign_3 = Signs.objects.create(Signatories_name=Signatories_name_3, digital_Signatures=digital_Signatures_3,
                                           event_name=event_name)
            create_sign_3.save()
        players = Players.objects.filter(event_name="None")
        for i in players:
            i.event_name = event_name
            i.save()
        dataset = Dataset()
        new_persons = request.FILES['myfile']
        imported_data = dataset.load(new_persons.read(), format='xlsx')
        for data in imported_data:
            value = Players(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],

            )
            value.save()
        messages.info(request,'Event added Succesfully')
        return redirect('preview')
    return render(request,'add_event.html',)

#@login_required(login_url='login')
def preview(request,):
    event_info = Event_details.objects.all()
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        event_details = Event_details.objects.filter(event_name=event_name)
        event_signs = Signs.objects.filter(event_name=event_name)
        context = {'event_details':event_details,'event_signs':event_signs,'event_info':event_info}
        return render(request, 'preview.html', context)
    return render(request,'preview.html',{'event_info':event_info})

#@login_required(login_url='login')
def edit_event(request,pk):
    event = Event_details.objects.get(id=pk)
    return render(request,'update.html',{'event_info':event})

#@login_required(login_url='login')
def edit_sign(request,pk):
    sign = Signs.objects.get(id=pk)
    return render(request,'update_sign.html',{'event_info':sign})

#@login_required(login_url='login')
def update_event(request,event_name):
    event_info = Event_details.objects.get(event_name=event_name)
    signs = Signs.objects.filter(event_name=event_name)
    players = Players.objects.filter(Q(event_name=event_name) | Q(event_name="None"))
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        event_start_date = request.POST.get('event_start_date')
        event_end_date = request.POST.get('event_end_date')
        organizer = request.POST.get('organizer')
        event_info.event_name = event_name
        event_info.event_start_date = event_start_date
        event_info.event_end_date = event_end_date
        event_info.organizer = organizer
        event_info.save()
        for i in signs:
            i.event_name = event_name
            i.save()
        for i in players:
            i.event_name = event_name
            i.save()
        messages.info(request,'Updated Succesfully')
        return redirect('preview')
    else:
        messages.info(request,' Something Went Wrong')

    return render(request,'update.html',)

#@login_required(login_url='login')
def update_sign(request,pk):
    signs = Signs.objects.get(id=pk)
    if request.method == 'POST':
        Signatories_name = request.POST.get('Signatories_name')
        digital_Signatures = request.POST.get('digital_Signatures')
        signs.Signatories_name = Signatories_name
        if digital_Signatures:
            signs.digital_Signatures = digital_Signatures
        signs.save()
        messages.info(request,'Updated Succesfully')
        return redirect('preview')
    return render(request,'update_sign.html',)


def download(request):
    if request.method== 'POST':
        Registration_number = request.POST.get('Registration_number')
        players= Players.objects.get(Registration_number=Registration_number)
        print(players)
        return render(request, 'cer.html', {"players": players})
    return render(request,'cer.html')


def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response

