import numpy as np
import sys


def calculate_bilinear_coeffs(d1, d2, d3, d4, p):

    # TODO PROBLEM Z INtERPRETACJA WYNIKOW

    a1 = d1[0]
    a2 = d2[0] - d1[0] 
    a3 = d4[0] - d1[0]  
    a4 = d1[0] - d2[0] + d3[0] - d4[0] 
    b1 = d1[1] 
    b2 = d2[1] - d1[1]  
    b3 = d4[1] - d1[1] 
    b4 = d1[1] - d2[1] + d3[1] - d4[1]


    A = b3*a4 - b4*a3
    B = b1*a4 - b2*a3 + b4*p[0] - b4*a1 + b3*a2 - a4*p[1]
    C = b1*a2 + b2*p[0] - b2*a1 - p[1]*a2

    coeff = [A, B, C]

    roots = np.roots(coeff)

    # TODO UWAGA NA WYLICZANIE b
    # moze sie wydarzyc ze obydwa roots spelniaja warunki ponizsze - co wtedy?
    # pierwsza koncpecja b nalezy do przedzialu [0,1] - wkodzie to uwzgledniono ale trzreba potwierdzic matematycznie

    if len(roots) == 2:
        if (roots[0] <= 1 and roots[0] >= 0) and ( roots[0]*a4+a2 != 0) and (roots[1] <= 1 and roots[1] >= 0) and (roots[1]*a4+a2 != 0):
           sys.exit('Brak b')
        else:   
            if (roots[0]<= 1 and roots[0] >= 0) and (roots[0]*a4+a2 != 0):
                b = roots[0]
            elif (roots[1]<= 1 and roots[1] >= 0) and (roots[1]*a4+a2 != 0):
                b = roots[1]
            else:
                sys.exit('Error 1')
    if len(roots) == 1:
        if roots <=1 and roots >= 0 and roots*a4+a2 != 0:
            b = roots
        else:
            sys.exit('Houston mamy problem')

    a = (p[0] - a1 - a3*b)/(a2 + b4*b)

    return a,b


if __name__ == "__main__":
    # calculate_bilinear_coeffs([1,7],[5,7],[5,1],[1,1],[3,4])
    a1,b1 = calculate_bilinear_coeffs([4,9],[10,9],[13,1],[1,1],[1,1])
    a2,b2 = calculate_bilinear_coeffs([4,9],[10,9],[13,1],[1,1],[10,9])
    
    print a1,b1
    print a2,b2
