from django.shortcuts import render, redirect, HttpResponse
from PIL import Image, ImageDraw, ImageFont
from medicine.models import Drug, Pharmacy


# Create your views here.
def index(request):
    """
    药品展示
    :param request:
    :return:
    """
    if request.method=='GET':
        drug = Drug.objects.all()
    return render(request, 'medicine/index.html', {"a": drug})


def look(request):
    """
    查看药品详情
    :param request:
    :return:
    """
    drug = Drug.objects.all()
    return render(request, 'medicine/look.html', {"drug": drug})


def add(request):
    """
    添加新药品
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'medicine/add.html')
    else:
        d_picture = request.POST.get('d_picture')
        d_p_price = request.POST.get('d_p_price')
        d_s_price = request.POST.get('d_s_price')
        d_name = request.POST.get('d_name')
        d_type = request.POST.get('d_type')
        d_describe = request.POST.get('d_describe')
        d_expiration_date = request.POST.get('d_expiration_date')
        d_detail = request.POST.get('d_detail')
        d_manufacturers = request.POST.get('d_manufacturers')
        d_explain = request.POST.get('d_explain')
        d_remarks = request.POST.get('d_remarks')
        s = Drug.objects.create(d_picture=d_picture, d_p_price=d_p_price, d_s_price=d_s_price, d_name=d_name, d_type=d_type,
                 d_describe=d_describe, d_expiration_date=d_expiration_date, d_detail=d_detail,
                 d_manufacturers=d_manufacturers, d_explain=d_explain, d_remarks=d_remarks)
        return render(request, 'medicine/index.html')


def append(request):
    """
    添加药品数量
    :param request:
    :return:
    """
    return render(request, 'medicine/add_medicine.html')
