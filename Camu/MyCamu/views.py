from django.shortcuts import render

def schedule_view(request):
    return render(request, 'MyCamu/schedule.html')