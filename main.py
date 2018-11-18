import math
import time
def sanjiaoxing() :
    time.sleep(0.5)
    vr=1
    while vr == 1 :
        print('请输入一个数字，我们将计算它的圆面积：')
        time.sleep(1)
        π=3.14
        r=int(input())
        if 10000000>= r > 0:
            pf=r*r
            print('获得半径为：',r)
            time.sleep(1)
            print('正在计算')
            time.sleep(3)
            print('圆的面积为:',pf*π)
            time.sleep(0.5)
            print('计算完成')
        else:
            print('计算失败')
            mune()

def mune():
    print('请选择你的计算方式')
    print('0.帮助')
    print('1.圆面积计算')
    print('2.正方形面积计算')
def square():
    while vr == 1:
        print('请输入两个数字，我们将计算它的四边形面积：')
        time.sleep(1)
        print('请输入a的长度')
        a=int(input())
        if a == 0:
            mune()
        else:
            time.sleep(0.5)
            print('请输入b的长度')
            b=int(input())
            print('获得长为',a ,'宽0为',b)
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
print('         1.禁止输入<0或>100000000的数')
print('         1.禁止输入字母')
time.sleep(0.5)
mune()
var=int(input())
if var == 1:
    sanjiaoxing()
elif var == 2 :
    square()
    