from django.shortcuts import render, redirect, HttpResponse
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
from django import views
from .models import *


def verify_code(request):
    """随机生成验证码"""
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，字体路径为”booktest/FreeMono.ttf”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    print(rand_str)
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    de = buf.getvalue()
    return HttpResponse(de, 'image/png')


def Login(request):
    """
    登录页面 \n
    """
    u_id = request.session.get("u_id")
    if u_id:
        return redirect('index')
    else:
        if request.method == 'GET':
            return render(request, 'login.html')

        else:
            vcode_input = request.POST.get('vcode')
            vcode_session = request.session.get('verifycode')
            if vcode_input != vcode_session:
                return render(request, 'login.html', {'b': "验证码不正确"})
            user = request.POST.get('user')
            password = request.POST.get('password')
            try:
                u = User.objects.get(user=user, password=password)

            except Exception:

                return render(request, 'login.html', {'a': '账号或密码错误'})
            else:
                request.session["u_id"] = u.id
                return redirect('index')


def register(request):
    """
    注册
    :param request:
    :return:
    """
    if request.method == 'GET':
        """判断表单请求状态"""
        role = Role.objects.all()
        return render(request, 'user/addUser.html', {'r': role})

    else:
        username = request.POST.get('username')
        try:
            u = User.objects.get(user=username)
        except Exception:
            # return HttpResponse('用户名已存在')
            password = request.POST.get('password')
            try:
                int(password[0])
            except:
                if not len(password) >= 10:
                    return HttpResponse('密码长度不能小于10')
                realname = request.POST.get('realname')
                email = request.POST.get('email')
                status = request.POST.get('status')
                role = request.POST.get('role')
                print(username, '+', password, '+', realname, "+", email, '+', status, '+', role)
                User.objects.create(user=username, password=password, name=realname, email=email, status=status,
                                    role_id=role)
                return HttpResponse('注册成功')

            else:
                role = Role.objects.all()
                return render(request, 'user/addUser.html', {'b': '密码不能以数字开头', 'r': role})
        else:
            role = Role.objects.all()
            return render(request, 'user/addUser.html', {'a': '用户名已存在', 'r': role})


def index(request):
    """首页显示"""
    u_id = request.session.get('u_id')
    if u_id:
        return render(request, 'index.html')
    else:
        return redirect('login')


def quit(request):
    """退出登录"""
    request.session.flush()
    return redirect('login')


def role_index(request):
    """角色信息首页"""
    a = Role.objects.all()  # 获取角色表中所有信息
    return render(request, 'role/index.html', {'a': a})


def dds(request, sid):
    """编辑角色权限"""
    if request.method == 'GET':
        a = Role.objects.get(id=sid)
        b = Jurisdiction.objects.all()

        return render(request, 'role/editRole.html', {'a': a, 'b': b})
    else:
        s = request.POST.getlist('group[]')
        a = Role.objects.get(id=sid)
        status = request.POST.get('status')
        a.r_status=status
        a.save()
        a.jurisdiction_set.clear()


        a.jurisdiction_set.add(*s)
        return HttpResponse(a.jurisdiction_set.all)




