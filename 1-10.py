import random

c = 0
f = 0
e = 0
while 1:
    n1 = random.randint(1, 9)
    n2 = random.randint(1, 9)
    c = c + 1
    a = int(input("%d X %d =? " %(n1,n2)))
    if a == n1 * n2 :
        f = f + 1
        b = input("맞췄습니다 계속하시겠습니까? 'Y'es or 'N'o :")
        if b == "Y" :
            continue
        elif b == "N" :
            e = f/c * 100
            print("정답률 %0.f%% " % e)
            break
        else :
            print("??")
    elif a == ' ':
        print("??")
    else :
        print("틀렸습니다 맞출때까지 끝나지않습니다.")

print("끝났습니다.")
