from wsgi_func.renderer import render
from wsgi_func.router import route
# wsgi_app.py
# environ - где вся информация о запросах хранится в качестве метода request, url, параметров запроса, и тому подобное
# start_response , который высылает предполагаемый ответ.
def wsgi_app(env, start_response):
    url = env.get('PATH_INFO')
    func = route(url)
    if callable(func):
        start_response('200 OK', [('Content-Type', 'text/html')])
        return func(env)