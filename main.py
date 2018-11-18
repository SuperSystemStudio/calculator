import math
import time
print('软件加载成功')
time.sleep(0.5)
print('作者：Mr.yan')
time.sleep(0.5)
print('使用规则：')
print('         1.禁止输入<0或>100000000的数')
print('         1.禁止输入字母')
time.sleep(0.5)
var=int(input())
while var == 1 :
    print('请输入一个数字，我们将计算它的圆面积：')
    time.sleep(1)
    a=3.14
    r=int(input())
    if 10000000>= r > 0:
        b=r*r
        print('获得半径为：',r)
        time.sleep(1)
        print('正在计算')
        time.sleep(3)
        print('圆的面积为:',b*a)
        time.sleep(0.5)
        print('计算完成')
    else:
        print('计算失败')
