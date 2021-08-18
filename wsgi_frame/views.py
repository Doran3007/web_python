from wsgi_func.renderer import render

def index(request):
    return render('index.html')