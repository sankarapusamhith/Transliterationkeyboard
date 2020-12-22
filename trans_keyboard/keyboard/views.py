from django.shortcuts import render
import json
import requests
from django.http import HttpResponse


# Create your views here.
def index(request):
    lang = [ 'telugu','hindi', 'tamil', 'bengali', 'gujarati', 'marathi', 'kannada', 'malayalam', 'punjabi', 'nepali']
    return render(request,'main.html',{'lang':lang})
def predict(request):
    clicked = None
    if request.method == "POST":
        clicked=request.POST['data']
        language=request.POST['lang']

        #Calling API to search for transliteration
        api = "http://xlit.quillpad.in/quillpad_backend2/processWordJSON?lang={0}&inString={1}".format(language,clicked)
        response = requests.get(str(api))
        output = (response.json())

        print(output)
        options = (output['twords'][0]['options'])
        itrans = output['itrans']

        if itrans not in options:
            options.append(itrans)
        

        return HttpResponse(json.dumps(options))