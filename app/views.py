from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q
def display_topic(request):
    QST=Topic.objects.all()
    QST=Topic.objects.filter(topic_name='Cricket')
    d={'topic':QST}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(topic_name='Cricket')
    QSW=Webpage.objects.exclude(topic_name='Cricket')
    QSW=Webpage.objects.all()[:5:]
    QSW=Webpage.objects.all().order_by('name')
    QSW=Webpage.objects.all().order_by('-name')
    QSW=Webpage.objects.filter(url__endswith='com')
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(url__startswith='http')
    QSW=Webpage.objects.filter(name__startswith='v')
    QSW=Webpage.objects.filter(name__endswith='i')
    QSW=Webpage.objects.filter(name__contains='a')
    QSW=Webpage.objects.filter(name__regex='\w{4}')
    QSW=Webpage.objects.filter(name__in=['vani','vijay','vyshu'])
    QSW=Webpage.objects.filter(Q(topic_name='Baseball') | Q (name='vani'))
    QSW=Webpage.objects.filter(Q(topic_name='Baseball') & Q (url__startswith='https'))
    QSW=Webpage.objects.all()
    d={'webpage':QSW}
    return render(request,'display_Webpage.html',d)

def display_AccessRecord(request):
    QSA=AccessRecords.objects.all()
    QSW=AccessRecords.objects.all().order_by('name')
    QSA=AccessRecords.objects.filter(date='2001-2-3')
    QSA=AccessRecords.objects.filter(date__gt='2001-2-3')
    QSA=AccessRecords.objects.filter(date__gte='2001-2-3')
    QSA=AccessRecords.objects.filter(date__lt='2005-2-3')
    QSA=AccessRecords.objects.filter(date__lte='2005-2-3')
    QSA=AccessRecords.objects.filter(date__year='2002')
    QSA=AccessRecords.objects.filter(date__month='2')
    #QSA=AccessRecords.objects.filter(date__year__get='2001')
    d={'AccessRecord':QSA}
    return render(request,'display_access.html',d)



def update_webpage(request):
    Webpage.objects.filter(name='vani').update(url='http://vani.in')
    Webpage.objects.filter(topic_name='Cricket').update(name='vani')
    Webpage.objects.filter(name='Baseball').update(name='vyshu')
    Webpage.objects.filter(topic_name='Rugby').update(name='kanna')
    Webpage.objects.filter(topic_name='Vollyball').update(name='sai')
    T=Webpage.objects.update_or_create((name='renuka'),defaults={'topic_name':'Football','url':'https:/renu.com'})
    T.save()
    QSW=Webpage.objects.all()
    d={'webpage':QSW}
    return render(request,'display_Webpage.html',d)