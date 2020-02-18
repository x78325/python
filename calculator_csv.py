import sys
import csv
import json
                                   #原始收入

salary = 0                         #税后收入
shouldpay = 0                      #应纳税所得额
tax=0                              #纳税金额

def calculator(num):
    shehou=num*(1-0.165)
    shouldpay = shehou-5000
    if shouldpay<=0:
        tax=0
    elif shouldpay<=3000:
        tax=shouldpay*0.03
    elif shouldpay<=12000:
        tax=shouldpay*0.1-210
    elif shouldpay<=25000:
        tax=shouldpay*0.2-1410
    elif shouldpay<=35000:
        tax=shouldpay*0.25-2660
    elif shouldpay<=55000:
        tax=shouldpay*0.3-4410
    elif shouldpay<=80000:
        tax=shouldpay*0.35-7160
    else :
        tax=shouldpay*0.45-15160
    salary=shehou-tax
    return '{:.2f}'.format(salary)
def chucun(data):
    sur_str=json.dumps(data)
    sur_json=sys.argv[2]
    with open(sur_json,'w') as j:
        j.write(sur_str)
def main():
    result={}
    
    with open (sys.argv[1]) as f:
        shouru=list (csv.reader(f))
    
        
    for item in shouru:
        id,income=item[0],float(item[1])
        result[id]=calculator(income)
    chucun(result)

main()

