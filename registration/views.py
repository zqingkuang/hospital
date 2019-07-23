from django.shortcuts import render, redirect, HttpResponse
from django import views
from .models import *
import re
from doctor.models import Doctor
from user.models import Section
from datetime import date

# Create your views here.


def index(request):
    '''
    门诊首页展示、挂号查询
    :param request:
    :return:
    '''
    if request.method =='GET':
        r = Registration.objects.all()
        return render(request,'registration/index.html',{'r':r})

    else:
        id = request.POST.get('id')
        name = request.POST.get('name')
        section = request.POST.get('section')
        if id:
            r = Registration.objects.filter(id=id)
            return render(request, 'registration/index.html', {"r": r})
        elif name and section:
            r = Registration.objects.filter(r_name__icontains=name,r_section__name__icontains=section)
            return render(request,'registration/index.html',{"r":r})
        elif name:
            r = Registration.objects.filter(r_name__icontains=name)
            return render(request,'registration/index.html',{"r":r})
        elif section:
            r = Registration.objects.filter(r_section__name__icontains=section)
            return render(request, 'registration/index.html', {"r": r})
        else:
            r = Registration.objects.all()
            return render(request, 'registration/index.html', {"r": r, 'error': '*有必填项未填入'})


def add(request):
    '''
    添加挂号人资料
    :param request:
    :return:
    '''
    if request.method =='GET':
        # r = Registration.objects.all()
        # return render(request,'registration/add.html',{'r':r})b
        r=Doctor.objects.all()
        s=Section.objects.all()
        return render(request,'registration/add.html',{'r':r,'s':s})
    else:
        name = request.POST.get('name') #姓名
        ID_number = request.POST.get('ID_number') #身份证号
        social_security = request.POST.get('social_security')  # 社保号
        registration_fee = request.POST.get('registration_fee')  # 挂号费
        phone = request.POST.get('phone')  # 联系电话
        self_paying = request.POST.get('self_paying')  # 是否自费
        sex = request.POST.get('sex')  # 性别
        age = request.POST.get('age')  # 年龄
        profession = request.POST.get('profession')  # 职业
        examination = request.POST.get('examination')  # 初复诊
        section = request.POST.get('section')  # 所挂科室
        doctor = request.POST.get('doctor')  # 指定医生
        remarks = request.POST.get('remarks')  # 备注
        print(name,ID_number,social_security,registration_fee,phone,self_paying,sex,age,profession,examination,section,doctor,remarks,)
        if not all([name,ID_number,social_security,registration_fee,phone,self_paying,sex,age,profession,examination,section,doctor,remarks]):  #条件信息填写不完整
            return render(request,'registration/add.html',{'errmsg':'信息填写不完整'})

        if len(ID_number)!= 18:
            r = Doctor.objects.all()
            s = Section.objects.all()
            return render(request,'registration/add.html',{'r':r,'s':s,'error':'身份证号长度不为18位'})
        try:
            int(ID_number[:17])
        except:
            r = Doctor.objects.all()
            s = Section.objects.all()
            return render(request,'registration/add.html',{'r':r,'s':s,'error':'您的身份证号包含非数字'})
        else:
            r = Doctor.objects.all()
            s = Section.objects.all()
            if ID_number[-1] not in '0123456789':
                if ID_number[-1] != 'X':
                    return render(request,'registration/add.html',{'r':r,'s':s,'error':'您身份证号最后一位既不是数字，也不是大写X'})

        #验证社保号
        if len(social_security)!= 10:
            r = Doctor.objects.all()
            s = Section.objects.all()
            return render(request,'registration/add.html',{'r':r,'s':s,'error_soc':'社保号长度不为10位'})
        try:
            int(social_security[:10])
        except:
            r = Doctor.objects.all()
            s = Section.objects.all()
            return render(request, 'registration/add.html', {'r': r, 's': s, 'error_soc': '您的社保号包含非数字'})

        #挂号费限制
        # if registration_fee > '100':
        #     r = Doctor.objects.all()
        #     s = Section.objects.all()
        #     return render(request,'registration/add.html',{'r': r, 's': s,'error_reg':'您输入的挂号费不能高于100元且不能包含非数字'})

        #手机号
        if len(phone)!= 10:
            r = Doctor.objects.all()
            s = Section.objects.all()
            return render(request,'registration/add.html',{'r':r,'s':s,'error_phone':'手机号长度不为10位'})
        try:
            int(phone[:10])
        except:
            r = Doctor.objects.all()
            s = Section.objects.all()
            return render(request, 'registration/add.html', {'r': r, 's': s, 'error_phone': '您输入的手机号包含非数字'})

        r=Registration()
        r.r_name=name
        r.r_ID_number=ID_number
        r.r_social_security=social_security
        r.r_registration_fee=registration_fee
        r.r_phone=phone
        r.r_self_paying=self_paying
        r.r_sex=sex
        r.r_age=age
        r.r_profession=profession
        r.r_examination=examination
        r.r_section=Section.objects.get(name=section)
        r.r_doctor_id=doctor
        r.r_remarks=remarks
        r.save()
        print(r)
        return render(request,'registration/add.html')



def look(request,sid):
    '''
    挂号人详情
    :param request:
    :return:
    '''
    b= Registration.objects.get(id=sid)
    s=Section.objects.all()
    r =Doctor.objects.all()
    return render(request,'registration/look.html',{'b':b,'s':s,'r':r})

def edit(request,sid):
    '''
    修改挂号人信息详情
    :param request:
    :return:
    '''
    if request.method == 'GET':
        c = Registration.objects.get(id=sid)
        s = Section.objects.all()
        r = Doctor.objects.all()

        return render(request,'registration/edit.html',{'c':c,'s':s,'r':r,'d':c.id})
    else:

        a = Registration.objects.get(id=sid)

        name = request.POST.get('name')  # 姓名
        a.r_name = name

        ID_number = request.POST.get('ID_number')  # 身份证号
        if len(ID_number)!= 18:
            r = Doctor.objects.all()
            s = Section.objects.all()
            #return render(request,'registration/add.html',{'r':r,'s':s,'error':'身份证号长度不为18位'})
            return HttpResponse('身份证号码长度不为18位')
        try:
            int(ID_number[:17])
        except:
            r = Doctor.objects.all()
            s = Section.objects.all()
            # return render(request,'registration/add.html',{'r':r,'s':s,'error':'您的身份证号包含非数字'})
            return HttpResponse('您的身份证号包含非数字')
        else:
            r = Doctor.objects.all()
            s = Section.objects.all()
            if ID_number[-1] not in '0123456789':
                if ID_number[-1] != 'X':
                    # return render(request,'registration/add.html',{'r':r,'s':s,'error':'您身份证号最后一位既不是数字，也不是大写X'})
                    return HttpResponse('您身份证号最后一位既不是数字，也不是大写X')
        a.r_ID_number = ID_number

        #更改社保号
        social_security = request.POST.get('social_security')  # 社保号
        # if len(social_security)!= 10:
        #     r = Doctor.objects.all()
        #     s = Section.objects.all()
        #     # return render(request,'registration/add.html',{'r':r,'s':s,'error_soc':'社保号长度不为10位'})
        #     return HttpResponse('社保号长度不为10位')
        # try:
        #     int(social_security[:10])
        # except:
        #     r = Doctor.objects.all()
        #     s = Section.objects.all()
        #     # return render(request, 'registration/add.html', {'r': r, 's': s, 'error_soc': '您的社保号包含非数字'})
        #     return HttpResponse('社保号包含非数字')
        a.r_social_security = social_security

        registration_fee = request.POST.get('registration_fee')  # 挂号费
        a.r_social_security = registration_fee

        phone = request.POST.get('phone')  # 联系电话
        if len(phone)!= 10:
            r = Doctor.objects.all()
            s = Section.objects.all()
            # return render(request,'registration/add.html',{'r':r,'s':s,'error_phone':'手机号长度不为10位'})
            return HttpResponse('手机号长度不为10位')
        try:
            int(phone[:10])
        except:
            r = Doctor.objects.all()
            s = Section.objects.all()
            # return render(request, 'registration/add.html', {'r': r, 's': s, 'error_phone': '您输入的手机号包含非数字'})
            return HttpResponse('您输入的手机号包含非数字')
        a.r_phone = phone


        self_paying = request.POST.get('self_paying')  # 是否自费
        a.r_self_paying=self_paying

        sex = request.POST.get('sex')  # 性别
        a.r_sex = sex

        age = request.POST.get('age')  # 年龄
        a.r_age = age

        profession = request.POST.get('profession')  # 职业
        a.r_profession = profession

        examination = request.POST.get('examination')  # 初复诊
        a.r_examination = examination

        section = request.POST.get('section')  # 所挂科室
        # a.r_section = section
        a.r_section = Section.objects.get(name=section)

        doctor = request.POST.get('doctor')  # 指定医生
        a.r_doctor_id=doctor

        remarks = request.POST.get('remarks')  # 备注
        a.r_remarks = remarks
        # if not all([name,ID_number,social_security,registration_fee,phone,self_paying,sex,age,profession,examination,section,doctor,remarks]):  #条件信息填写不完整
        #     return HttpResponse('信息不完整')
        a.save()
        return render(request,'registration/index.html')

def delete(request,sid):

        Registration.objects.filter(id=sid).delete()
        return render(request,'index.html')
def registrations(request,page_no):
    page_size = 6
    reg = Registration.objects.all()
    num_reg = range(1,len(reg)//page_size+2)
    reg = reg[(page_no-1)*page_size:page_no*page_size]
    print('reg=',reg)
    print(num_reg)
    return render(request,'registration/index.html',{'page_no':page_no,'reg':reg})




def h_index(request):
    '''
    住院首页展示、住院查询
    :param request:
    :return:
    '''
    if request.method =='GET':
        h = Hospital.objects.all()
        # h = Hospital.objects.filter(h_status=1)
        # h1 = Hospital.objects.filter(h_status=2)
        # h2 = Hospital.objects.filter(h_status=3)
        return render(request,'hospital/index.html',{'h':h})
    else:
        id = request.POST.get('d_id')
        name = request.POST.get('d_name')
        section = request.POST.get('d_section')
        if id:
            h = Hospital.objects.filter(h_registration_id=id)
            return render(request, 'hospital/index.html', {"h": h})
        elif name and section:
            h = Hospital.objects.filter(h_registration__r_doctor__user__name__icontains=name,h_registration__r_section__name__icontains=section)
            return render(request,'hospital/index.html',{"h": h})
        elif name:
            h = Hospital.objects.filter(h_registration__r_doctor__user__name__icontains=name)
            return render(request,'hospital/index.html',{"h": h})
        elif section:
            h = Hospital.objects.filter(h_registration__r_section__name__icontains=section)
            return render(request, 'hospital/index.html', {"h": h})
        else:
            h = Hospital.objects.all()
            return render(request, 'hospital/index.html', {"h": h, 'error': '*有必填项未填入'})

def adds(request):
    if request.method == 'GET':
        h = Hospital.objects.all()
        s = Section.objects.all()
        r = Doctor.objects.all()
        return render(request, 'hospital/adds.html', {"h": h,'s':s,'r':r})
    else:
        id = request.POST.get('id')
        a = Hospital.objects.get(h_registration_id=id)
        return render(request, 'hospital/adds.html', {"a": a})




