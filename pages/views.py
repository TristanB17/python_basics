from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Yo wutup?')

# Create your views here.
