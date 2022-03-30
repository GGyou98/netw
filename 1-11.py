a = input("파일명 입력:")
try :
    f = open(a, "r")
    b = 1
    line = f.readline()
    while c:
        print("%d %s"%(b,line))
        line = f.readline()
        b = b + 1
        f.close()
except :
    print("그런거 없습니다.")