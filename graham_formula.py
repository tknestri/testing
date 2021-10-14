def graham_formula(eps,g,y):
    result = 7+g
    result = eps*4.4*result
    result /= y
    return result

# in_eps = float(input("Eanrings per share: "))
# in_growthr = float(input("Expected growth rate: "))
# in_y = float(input("Yield on AAA corprate bonds: "))
# print(graham_formula(in_eps,in_growthr,in_y))