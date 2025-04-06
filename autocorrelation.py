from imports import math

def f_function(N, d, f, flag):
    f_sum = 0
    if flag == 0:
        temp = 0
    else:
        temp = d
    for i in range(N - d):
        f_sum = f_sum + f[temp + i][1]
    return (1 / (N - d + 1)) * f_sum


def autocorrelation_function(f):
    N = len(f)
    Nd = int(N / 2)
    r = []

    #print(N) 339
    #print(Nd) 169

    for d in range(Nd):
        top = 0
        bottom = 0
        temp_b1 = 0
        temp_b2 = 0

        for j in range(N - d):
            #FORMULA TOP PART
            temp = (f[j][1] - f_function(N, d, f, 0)) * (f[d + j][1] - f_function(N, d, f, 1))
            top = top + temp
            
            #FORMULA BOTTOM PART
            temp = (f[j][1] - f_function(N, d, f, 0)) ** 2
            temp_b1 = temp_b1 + temp
            temp = (f[d + j][1] - f_function(N, d, f, 1)) ** 2
            temp_b2 = temp_b2 + temp
        bottom = math.sqrt(temp_b1 * temp_b2)
               
        r.append([d, top / bottom])
    return r