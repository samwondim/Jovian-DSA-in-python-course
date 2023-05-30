def multiply_basic(poly1, poly2):
    deg1 = len(poly1) - 1
    deg2 = len(poly2) - 1
    
    result = [0] * (deg1 + deg2 + 1)
    
    for i in range(deg1 + 1):
        for j in range(deg2 + 1):
            result[i+j] += poly1[i] * poly2[j]
    return result

def add(poly1, poly2):
    """Add two polynomials"""
    result = [0] * max(len(poly1), len(poly2))
    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]
    return result

def split(poly1, poly2):
    """Split each polynomial into two smaller polynomials"""
    mid = max(len(poly1), len(poly2)) // 2
    return  (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])

def increase_exponent(poly, n):
    """Multiply poly1 by x^n"""
    return [0] * n + poly

def multiply_optimized(poly1, poly2):
    if len(poly1) == 0 and len(poly2) != 0:
        return []
    elif len(poly2) == 0 and len(poly1) != 0:
        return []
    else:
        return optimized_function(poly1, poly2)

def optimized_function(poly1, poly2):
    n = max(len(poly1), len(poly2))

    if n == 1 or len(poly2) == 1 or n == 0 or len(poly2) == 0:
        return multiply_basic(poly1, poly2)
    
    (A0, A1), (B0, B1) = split(poly1, poly2)

    y = multiply_optimized(add(A0, A1), add(B0,B1))
    u = multiply_optimized(A0, B0)
    z = multiply_optimized(A1, B1)

    z_exp = increase_exponent(z, 2*(n//2))
    y_exp = increase_exponent(add(y, [-x for x in add(u,z)]), n//2)
    result = add(add(u, y_exp), z_exp)

    return result 


