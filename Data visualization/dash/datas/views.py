from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect
from.models import mydata
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.
import operator
import collections

@login_required(login_url="letmein")
def home(request):
#get all topic
    topics=mydata.objects.all()
    listtopic=[]
    for k in topics:
        listtopic.append(k.topic)
    topicsat= set()
    for itopic in topics:
        topicsat.add(itopic.topic)
    topiclist=[]
    for jtopic in topicsat:
        if jtopic=="":
            pass
        else:
            topiclist.append(jtopic)
    #count Topic
    dctopic={}
    for topiccount in topiclist:
        num=listtopic.count(topiccount)
        dctopic[topiccount]=num
    # print([dc.keys()])
    # print([dc.values()])
    sorted_topic = dict(sorted(dctopic.items(), key=operator.itemgetter(1), reverse=True))
    finallist=[]
    finallist2=[]
    for vtopic in sorted_topic:
        finallist.append(vtopic)
        finallist2.append(sorted_topic[vtopic])

#Country
    country = mydata.objects.all()
    listcountry = []
    for kcountry in country:
        listcountry.append(kcountry.country)
    countrysat = set()
    for icountry in country:
        countrysat.add(icountry.country)
    countrylist = []
    for jcountry in countrysat:
        if jcountry == "":
            pass
        else:
            countrylist.append(jcountry )
# count Topic
    dccountry = {}
    for count in countrylist:
        num = listcountry.count(count)
        dccountry[count] = num
    # print([dc.keys()])
    # print([dc.values()])
    sorted_country = dict(sorted(dccountry .items(), key=operator.itemgetter(1), reverse=True))
    contryname = []
    countrycount = []
    for vcountry  in sorted_country :
        contryname.append(vcountry )
        countrycount.append(sorted_country [vcountry ])
#source
    source = mydata.objects.all()
    listsource = []
    for ksource in source:
        listsource.append(ksource.source)
    sourcesat = set()
    for isource in source:
        sourcesat.add(isource.source)
    sourcelist = []
    for jsource in sourcesat:
        if jsource == "":
            pass
        else:
            sourcelist.append(jsource)
# count Topic
    dcsource = {}
    for countsource in sourcelist:
        num = listsource.count(countsource)
        dcsource[countsource] = num
    # print([dc.keys()])
    # print([dc.values()])
    sorted_source = dict(sorted(dcsource.items(), key=operator.itemgetter(1), reverse=True))
    sourcename = []
    sourcecount = []
    for vsource in sorted_source:
        sourcename.append(vsource)
        sourcecount.append(sorted_source[vsource])
#published year count
    yearp = mydata.objects.all()
    str=""
    plist =[]
    for pi in yearp:
        if pi.published=="":
            pass
        else:
            plist.append(pi.published)
            str=str+pi.published

    yearset=set()
    for di in plist:
        new=di.split()
        yearset.add(new[2])
    allyear=[]
    for year in yearset:
        allyear.append(year)
    countyear=[]
    newdict={}
    for iyear in allyear:
        countyear.append(int(str.count(iyear)))
        newdict[int(iyear)]=str.count(iyear)

    sor=collections.OrderedDict(sorted(newdict.items()))

    print(sor)
    sortyear = []
    sortyearcount = []
    for k, v in sor.items():
        sortyear.append(k)
        sortyearcount.append(v)


    context={"link":finallist2,"finallist":finallist,"all":topics,"country":contryname,"count":countrycount,"sourcelist":sourcename,"sourcecount":sourcecount,"years":sortyear,"countyear":sortyearcount}
    return render(request,"home.html",context)

@login_required(login_url="letmein")
def country(request):
    topics = mydata.objects.all()
    context={"all":topics}
    return render(request,"table.html",context)


@login_required(login_url="letmein")
def me(request):
    return render(request,"me.html")


def letmein(request):
        if request.method == "POST":
            name = request.POST.get("username")
            password = request.POST.get("passward")
            print(name)
            print(password)
            user = authenticate(username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                context={"msg":"There is no any user of this name"}
                return render(request, "letmein.html",context)
        return render(request, "letmein.html")

def letmeout(request):
    logout(request)
    return redirect("letmein")


