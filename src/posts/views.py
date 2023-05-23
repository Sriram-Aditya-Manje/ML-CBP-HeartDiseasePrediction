from django.shortcuts import render

from .models import Form, Post

import pickle

def post_list_view(request):
    post_objects=Post.objects.all()
    context={
        'post_objects':post_objects
    }
    return render(request,"posts/index.html",context)


def getPrediction(age,sex,cp,bp,col,fbs,ekg,mhr,ex,stdep,slop,num,thal):
    knnClassifier=pickle.load(open('posts/knnClassifier.pkl', 'rb'))
    ans=knnClassifier.predict([[age,sex,cp,bp,col,fbs,ekg,mhr,ex,stdep,slop,num,thal]])
    if ans==1:
        return "You may have heart disease"
    elif ans==0:
        return "You may not have heart disease"
    else:
        return "Error in prediction"


def form(request):
    form_objects=Form.objects.all()
    # knnClassifier=pickle.load(open('posts/knnClassifier.pkl', 'rb'))
    context={
        'form_objects':form_objects,
        # 'knnClassifier':knnClassifier
    }
    return render(request,"posts/form.html",context)

def result(request):
    try:
        age=int(request.GET['age'])
        sex=int(request.GET['sex'])
        cp=int(request.GET['cp'])
        bp=int(request.GET['bp'])
        col=int(request.GET['col'])
        fbs=int(request.GET['fbs'])
        ekg=int(request.GET['ekg'])
        mhr=int(request.GET['mhr'])
        ex=int(request.GET['ex'])
        stdep=float(request.GET['stdep'])
        slop=int(request.GET['slop'])
        num=int(request.GET['num'])
        thal=int(request.GET['thal'])

        result=getPrediction(age,sex,cp,bp,col,fbs,ekg,mhr,ex,stdep,slop,num,thal)

        return render(request,"posts/result.html",{'result':result})
    except:
        return render(request,"posts/result.html",{'result':'Something went wrong'})

def stats(request):
    
    DBURL = "mongodb+srv://vnr2022:vnr2022@shivacluster.zijeq.mongodb.net/admin?authSource=admin&replicaSet=atlas-unyjbr-shard-0&w=majority&readPreference=primary&retryWrites=true&ssl=true"

    # CONNECTION AND CREATION OF DATABASE
    from pymongo import MongoClient
    import pymongo

    client = pymongo.MongoClient(DBURL)

    db = client.summerdb
    coll = db['collection']
    s = list(coll.find())

    ages=[0]*10
    try:
        for i in s:
            ages[i['age']//10]+=1
    except:
        print()

    sex=[0,0]
    try:
        for i in s:
            sex[i['sex']]+=1
    except:
        print()

    age,bp=[],[]
    try:
        for i in s:
            age.append(i['age'])
            bp.append(i['bp'])
    except:
        print()

    return render(request,"posts/stats.html",{'ages':ages,'sex':sex,'agebp_age':age,'agebp_bp': bp})

def header(request):
    return render(request,"posts/header.html")