from django.shortcuts import render, redirect, HttpResponse,reverse
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
        return render(request, 'medicine/index.html',{'a':drug})
    else:
        name=request.POST.get('d_name')
        a=Drug.objects.filter(d_name__icontains=name)
        return render(request,'medicine/index.html',{'a':a})

def drugs(request,page_no):
    """根据页码返回数据"""
    if request.method == 'GET':
        page_size = 6
        drugs1 = Drug.objects.all()
        num_drugs = [i for i in range(1,len(drugs1)//page_size+2)]
        drugs = drugs1[(page_no-1)*page_size:page_no*page_size]
        print('drugs=',drugs)
        print(page_no,len(drugs1)//6+1)
        return render(request,'medicine/index.html',{'page_no':page_no,'a':drugs,'n':num_drugs,'m':len(drugs1)//6+1,'page_on0':page_no-1,'page_on1':page_no+1,'f':len(drugs1)})


def look(request,sid):
    """
    查看药品详情
    :param request:
    :return:
    """

    d = Drug.objects.get(id=sid)
    return render(request, 'medicine/look.html', {"b":d})


def add(request):
    """
    添加新药品
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'medicine/add.html')
    else:
        d_picture = request.FILES.get('d_picture')
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
        d_inventory=request.POST.get('d_inventory')
        d_status=request.POST.get('d_status')
        d_number = request.POST.get('d_number')
        if not all([d_picture,d_p_price,d_s_price,d_name,d_type,d_describe,d_expiration_date,d_detail,d_manufacturers,d_explain,d_remarks,d_inventory,d_status,d_number]):
            return render(request,'registration/add.html',{'errmsg':'信息填写不完整'})
        s = Drug.objects.create(d_picture=d_picture, d_p_price=d_p_price, d_s_price=d_s_price, d_name=d_name, d_type=d_type,
                 d_describe=d_describe, d_expiration_date=d_expiration_date, d_detail=d_detail,
                 d_manufacturers=d_manufacturers, d_explain=d_explain, d_remarks=d_remarks,d_inventory=d_inventory,d_status=d_status,d_number=d_number)
        return redirect('mindex')




def append(request,sid):
    """
    添加药品数量
    :param request:
    :param sid:
    :return:
    """

    if request.method == 'GET':
        b = Drug.objects.get(id=sid)
        return render(request, 'medicine/add_medicine.html', {'b': b})
    else:
        n=request.POST.get('d_inventory')
        b = Drug.objects.get(id=sid)
        b.d_inventory = b.d_inventory+int(n)
        b.save()

        return redirect('mindex')

def update(request,sid):
    """
    修改药品信息
    :param request:
    :return:
    """
    if request.method == 'GET':
        c=Drug.objects.get(id=sid)
        return render(request, 'medicine/update.html',{'b':c})
    else:
        d_picture = request.FILES.get('d_picture')
        print(d_picture)
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
        d_inventory = request.POST.get('d_inventory')
        d_status = request.POST.get('d_status')
        d_number = request.POST.get('d_number')
        c = Drug.objects.get(id=sid)
        c.d_picture=d_picture
        c.d_p_price=d_p_price
        c.d_s_price=d_s_price
        c.d_name=d_name
        c.d_type=d_type
        c.d_describe=d_describe
        c.d_expiration_date=d_expiration_date
        c.d_detail=d_detail
        c.d_manufacturers=d_manufacturers
        c.d_explain=d_explain
        c.d_remarks=d_remarks
        c.d_inventory=d_inventory
        c.d_status=d_status
        c.d_number=d_number
        c.save()
        return redirect('mindex')


