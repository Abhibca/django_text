from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunch = request.GET.get('removepunch', 'off')
    capitalizefirst = request.GET.get('capitalizefirst', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')
    print(djtext)

    #analyzed = djtext
     

    if(removepunch == "on"):
        punctuation = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'perpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)

    if(capitalizefirst == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'perpose': 'Changed Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        params = {'perpose': 'Nwe Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)

    if(spaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'perpose': 'Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)

    if(charcount == "on"):
        analyzed = ""
        for char in djtext:
           analyzed = str(len(analyzed + char)+1)
        params = {'perpose': 'Charecter Count', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)

    if(removepunch != "on" and capitalizefirst !="on" and newlineremover !="on" and spaceremover !="on" and charcount !="on"):
        return HttpResponse("Error HE bhai")

    return render(request, 'analyze.html', params)