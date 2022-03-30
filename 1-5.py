def Tc(n):
    tc=(5/9) * (n-32)
    return tc

def Tf(n):
    tf=(9/5) * (n+32)
    return tf

a = int(input("Enter a temperature: "))
b = input("Convert to (F)ahrenheit or (C)elsius?: ")
if b == "F" :
    print(Tf(a))
elif b == "C" :
    print(Tc(a))
else :
    print("플리즈 에프 오어 씨 엔터 온리")
