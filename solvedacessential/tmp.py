def tri_system(number):
    q, r = divmod(number, 3)
    n = str(r)
    return tri_system(q) + n if q else n

tri_system(10)