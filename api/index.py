# api/index.py
from mysite.wsgi import application

def handler(event, context):
    # Vercel WSGI handler
    from mangum import Mangum
    asgi_handler = Mangum(application)
    return asgi_handler(event, context)
