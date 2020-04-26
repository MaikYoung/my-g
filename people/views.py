from django.shortcuts import render

from people.models import Gender


def genders_render(request):
    genders = Gender.objects.all()
    context = {'genders': genders}
    return render(request, 'people/people.html', context)
