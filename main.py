import time
import os
import basic
basic.remove()
# Global variable list
pai=3.14    #This is π
# function list
def yuanxing() :
    time.sleep(0.5)
    vr=1
    while vr == 1 :
        print('请输入一个数字，我们将计算它的圆面积：')
        time.sleep(1)
        r=eval(input())
        if 10000000>= r >0:
            print('获得半径为：',r)
            time.sleep(1)
            print('正在计算')            
            time.sleep(3)
            print(pai*r*r)
            time.sleep(0.5)
            print('计算完成')
        elif r == 0:
            vr=vr-1
            menu()
        else:
            print('error')               
def menu():
    print('请选择你要选择的选项')
    print('0.返回上级菜单')
    print('1.圆面积计算')
    print('2.正方形面积计算')
    print('3.圆的表面积计算')
    print('4.关闭程序')
    print('5.设置')
    var=int(input())
    if var == 1 :
        yuanxing()
    elif var == 2 :
        square()
    elif var == 0:
        menu()
    elif var == 3:
        yuanbiaomianji()
    elif var == 4:
        print('are you sure?')
        print('1.yes')
        print('2.no')
        choose=int(input())
        if choose == 1:
            os._exit(0)
        elif choose == 2:
            menu()
    elif var == 5:
        print('1.设置语言')
        var=int(input())
        if var == 0:
            menu()
        elif var == 1:
            basic.language
            pass
def square():
    vr=1
    while vr == 1:
        print('请输入两个数字，我们将计算它的四边形面积：')
        print('请输入a的长度')
        a=eval(input())
        if a == 0:
            vr=vr-1
            menu()
        else:
            time.sleep(0.5)
            print('请输入b的长度')
            b=eval(input())
            if b == 0:
                vr=vr-1
                menu()
            else:    
                print('长为',a ,'宽为',b)
                time.sleep(1)
                print('正在计算')
                time.sleep(3)
                print('四边形的面积为:',a*b)
                time.sleep(0.5)
                print('计算完成')
def yuanbiaomianji():
    vr=1
    while vr == 1:
        print('正在加载')
        time.sleep(0.5)
        print('请输入半径')
        r=eval(input())
        if 10000000>= r >0:
            pf=r*r
            print('获得半径为：',r)
            time.sleep(1)
            print('正在计算')
            time.sleep(0.5)
            print('计算完成')
            yuanmianji=pf*pai
            print('请输入长')
            a=eval(input())
            if a == 0:
                menu()
            else:
                print('请输入宽')
                b=eval(input())
                if b == 0:
                    menu()
                else:
                    print('正在计算')
                    print('圆的表面积为',a*b+2*yuanmianji)
        elif r == 0:
            vr=vr-1
            menu()
        else:
            print('error')
# head
print('软件加载成功')
time.sleep(0.5)
print('作者：Mr.yan')
time.sleep(0.5)
print('使用规则：')
print('         1.禁止输入<0或>100000000的数')
print('         2.禁止输入字母')
print('         3.禁止输入类似于05、04这样的文字')
time.sleep(0.5)
menu()
