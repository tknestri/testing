import math

def graham_number(eps,bvps):
    result = 15.0*1.5*eps*bvps
    result = math.sqrt(result)
    return result

print("Result WILL be invalid if p/e ratio> 15\nResult WILL be invalid if price to book ratio>1.5")
a = float(input("Earnings per share: "))
b = float(input("Book value per share: "))
print(graham_number(a,b))