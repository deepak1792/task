from django.contrib.auth.models import User
from django.http import JsonResponse
from exceptionlog import utils
from example.models import *
import json

def addobject(request):
    res = {}
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            rc = Object()
            rc.name = data['name']
            rc.description = data['description']
            rc.slug = data['slug']
            rc.user = User.objects.get(pk=int(data['id']))
            rc.save()
            res['status']=1
        except:
            utils.PutException()
            res['status'] = 0
        return JsonResponse(res)

def getobject(request):
    res={}
    try:
        rec=Object.objects.all()
        mlist=[]
        for i in rec:
            temp={}
            temp['name']=i.name
            temp['date']=utils.formalDateWithTime(i.date)
            temp['description']=i.description
            temp['activated']=i.activated
            temp['slug']=i.slug
            mlist.append(temp)
        res['status']=1
        res['data']=mlist
    except:
        utils.PutException()
        res['status'] = 0
    return JsonResponse(res)
