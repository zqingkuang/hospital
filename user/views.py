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


class Login(views.View):
    """
    登录页面 \n
    """

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        vcode_input = request.POST.get('vcode')
        vcode_session = request.session.get('verifycode')
        if vcode_input != vcode_session:
            return render(request, 'login.html', {'b': "验证码不正确"})
        user = request.POST.get('user')
        password = request.POST.get('password')
        try:
            u = User.objects.get(user=user, password=password)

        except:
            return render(request, 'login.html', {'a':'账号或密码错误'})
        else:
            return HttpResponse('登录成功')
