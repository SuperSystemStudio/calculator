import math
import time
import os
def sanjiaoxing() :
    time.sleep(0.5)
    vr=1
    while vr == 1 :
        print('请输入一个数字，我们将计算它的圆面积：')
        time.sleep(1)
        π=3.14
        r=eval(input())
        if 10000000>= r >0:
            pf=r*r
            print('获得半径为：',r)
            time.sleep(1)
            print('正在计算')
            time.sleep(3)
            print('圆的面积为:',pf*π)
            time.sleep(0.5)
            print('计算完成')
        elif r == 0:
            vr=vr-1
            mune()
        else:
            print('计算失败')               
def mune():
    print('请选择')
    print('0.返回上级菜单')
    print('1.圆面积计算')
    print('2.正方形面积计算')
    print('3.退出程序')
    var=int(input())
    if var == 1 :
        sanjiaoxing()
    elif var == 2 :
        square()
    elif var == 0:
        mune()
    elif var == 3:
        os._exit(0)
def square():
    vr=1
    while vr == 1:
        print('请输入两个数字，我们将计算它的四边形面积：')
        print('请输入a的长度')
        a=eval(input())
        if a == 0:
            vr=vr-1
            mune()
        else:
            time.sleep(0.5)
            print('请输入b的长度')
            b=eval(input())
            if b == 0:
                vr=vr-1
                mune()
            else:    
                print('长为',a ,'宽为',b)
                time.sleep(1)
                print('正在计算')
                time.sleep(3)
                print('四边形的面积为:',a*b)
                time.sleep(0.5)
                print('计算完成')
print('软件加载成功')
time.sleep(0.5)
print('作者：Mr.yan')
time.sleep(0.5)
print('使用规则：')
print('         1.禁止输入>100000000或<0的数')
print('         1.禁止输入字母')
time.sleep(0.5)
mune()
var=int(input())
if var == 1:
    sanjiaoxing()
elif var == 2 :
    square()
elif var == 0:
    mune()
elif var == 3:
    os._exit(0)
