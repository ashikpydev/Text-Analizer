from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def analyze(request):
    #get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'removed puntuations', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")

