from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    html = "<h1>Welcome to the snowboarding and downhill skiing club</h1><br><p>Here you will learn a lot about snowboarding and downhill skiing</p>"
    return HttpResponse (html)

def about(request):
    logger.exception(f'About page accessed')
    html = "<p>Hi, we are a team of experienced snowboarding and downhill skiing instructors.Here we share our impressions of ski resorts and show you how to ski properly. By the way, you can sign up for our classes using the link in the profile header.</p>"
    return HttpResponse(html)



