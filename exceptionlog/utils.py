from .models import exceptionlogs
import linecache
import sys

def timeFormat(t):
    newT = t.strftime("%d %b, %I:%M %p")
    return newT

def formalDate(t):
    newT = t.strftime("%d - %m - %Y")
    return newT

def formalDateWithTime(t):
    newT = t.strftime("%d - %m - %Y, %H:%M")
    return newT

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def PutException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    try:
        ex_rec=exceptionlogs()
        ex_rec.filename=filename
        ex_rec.lineno = lineno
        ex_rec.code = line.strip()
        ex_rec.type = exc_obj
        ex_rec.save()
    except:
        print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))
