import math
def area():
    a=0
    while a==0 :
        try:
            r=input('输入园的半径： ')
            area=int(r)**2*math.pi
            a=1
        except:
            print('请输入整数作为半径！')

    print('园的面积等于{:.2f}'.format(area))
if __name__=='__main__':
    area()

