def S(n):
    S=4 * (n ** 2)
    return S

def V(n):
    V=4/3 * (n ** 3)
    return V

a = int(input("반지름: "))
print("겉면적: %dπ, 부피: %dπ " % (S(a),V(a)))