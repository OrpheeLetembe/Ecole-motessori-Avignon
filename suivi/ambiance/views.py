from django.shortcuts import render


from .models import Ambiance


def ambiance_list(request):
    ambiances = Ambiance.objects.all()
    return render(request, 'ambiance/all.html', context={'ambiances': ambiances})
