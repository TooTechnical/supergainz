from django.shortcuts import render
from django.http import JsonResponse

def subscribe_newsletter(request):
    return JsonResponse({"success": True})


# Create your views here.
