from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from products.models import Cakmak, Marka
from django.db.models import Q


def home(request):
    queryset_list = Cakmak.objects.filter(insert=True)
    paginator = Paginator(queryset_list, 24)
    page = request.GET.get('page')

    try:
        cakmak = paginator.page(page)
    except PageNotAnInteger:
        cakmak = paginator.page(1)
    except EmptyPage:
        cakmak = paginator.page(paginator.num_pages)

    marka = Marka.objects.all()
    context = {
        'cakmak': cakmak,
        'marka': marka
    }
    return render(request, 'index.html', context)


def cakmak(request, no):
    cakmak = get_object_or_404(Cakmak, no=no)

    marka = Marka.objects.all()
    context = {
        'cakmak': cakmak,
        'marka': marka
    }

    return render(request, 'cakmak.html', context)


def arama(request):
    queryset_list = Cakmak.objects.all()

    if 'arama' in request.GET:
        arama = request.GET.get('arama')
        if arama:
            queryset_list = queryset_list.filter(
                Q(marka__icontains=arama) | Q(model__icontains=arama) | Q(no__icontains=arama))

    paginator = Paginator(queryset_list, 24)
    page = request.GET.get('page')

    try:
        cakmak = paginator.page(page)
    except PageNotAnInteger:
        cakmak = paginator.page(1)
    except EmptyPage:
        cakmak = paginator.page(paginator.num_pages)

    marka = Marka.objects.all()
    context = {
        'cakmak': cakmak,
        'marka': marka
    }
    return render(request, 'index.html', context)


def marka(request):
    queryset_list = Cakmak.objects.all()

    if 'marka' in request.GET:
        arama = request.GET.get('marka')
        if arama:
            queryset_list = queryset_list.filter(marka__icontains=arama)

    paginator = Paginator(queryset_list, 24)
    page = request.GET.get('page')

    try:
        cakmak = paginator.page(page)
    except PageNotAnInteger:
        cakmak = paginator.page(1)
    except EmptyPage:
        cakmak = paginator.page(paginator.num_pages)

    marka = Marka.objects.all()
    context = {
        'cakmak': cakmak,
        'marka': marka
    }
    return render(request, 'index.html', context)


def plastik(request):
    queryset_list = Cakmak.objects.filter(materyal__exact='Plastik')
    paginator = Paginator(queryset_list, 24)
    page = request.GET.get('page')

    try:
        cakmak = paginator.page(page)
    except PageNotAnInteger:
        cakmak = paginator.page(1)
    except EmptyPage:
        cakmak = paginator.page(paginator.num_pages)

    marka = Marka.objects.all()
    context = {
        'cakmak': cakmak,
        'marka': marka
    }
    return render(request, 'index.html', context)


def metal(request):
    queryset_list = Cakmak.objects.filter(materyal__exact='Metal')
    paginator = Paginator(queryset_list, 24)
    page = request.GET.get('page')

    try:
        cakmak = paginator.page(page)
    except PageNotAnInteger:
        cakmak = paginator.page(1)
    except EmptyPage:
        cakmak = paginator.page(paginator.num_pages)

    marka = Marka.objects.all()
    context = {
        'cakmak': cakmak,
        'marka': marka
    }
    return render(request, 'index.html', context)


def tasli(request):
    queryset_list = Cakmak.objects.filter(fonksiyon__exact='Taşlı')
    paginator = Paginator(queryset_list, 24)
    page = request.GET.get('page')

    try:
        cakmak = paginator.page(page)
    except PageNotAnInteger:
        cakmak = paginator.page(1)
    except EmptyPage:
        cakmak = paginator.page(paginator.num_pages)

    marka = Marka.objects.all()
    context = {
        'cakmak': cakmak,
        'marka': marka
    }
    return render(request, 'index.html', context)


def manyetolu(request):
    queryset_list = Cakmak.objects.filter(fonksiyon__exact='Manyetolu')
    paginator = Paginator(queryset_list, 24)
    page = request.GET.get('page')

    try:
        cakmak = paginator.page(page)
    except PageNotAnInteger:
        cakmak = paginator.page(1)
    except EmptyPage:
        cakmak = paginator.page(paginator.num_pages)

    marka = Marka.objects.all()
    context = {
        'cakmak': cakmak,
        'marka': marka
    }
    return render(request, 'index.html', context)


def rezistansli(request):
    queryset_list = Cakmak.objects.filter(fonksiyon__exact='Rezistanslı')
    paginator = Paginator(queryset_list, 24)
    page = request.GET.get('page')

    try:
        cakmak = paginator.page(page)
    except PageNotAnInteger:
        cakmak = paginator.page(1)
    except EmptyPage:
        cakmak = paginator.page(paginator.num_pages)

    marka = Marka.objects.all()
    context = {
        'cakmak': cakmak,
        'marka': marka
    }
    return render(request, 'index.html', context)


def iletisim(request):
    return render(request, 'iletisim.html')
