import time
b =open("test.txt", "r")
c =open("testexit.txt", "r")
b1 =open("test1.txt", "r")
c1 =open("testexit1.txt", "r")
b2 =open("test2.txt", "r")
c2 =open("testexit2.txt", "r")
b3 =open("test3.txt", "r")
c3 =open("testexit3.txt", "r")
def tbh(a):
    if (0<=a<=50):
        return 2
    if (50<a<=100):
        return 45
    if (100<a<=150):
        return 50
    if (150<a<=200):
        return 55
    if (200<a<=250):
        return 6
    if (250<a<=300):
        return 65
    if (300<a<=350):
        return 70
    if (350<a<=400):
        return 75
    if (400<a<=450):
        return 80
    if (450<a<=500):
        return 85
    else:
        return 90

def op1():
    d = b.read()
    e = int(d)
    f = c.read()
    g = int(f)
    return tbh(e-g)


#print(A)
#print(op1())
def op2():
    d1 = b1.read()
    e1 = int(d1)
    f1 = c1.read()
    g1 = int(f1)
    return tbh(e1-g1)
#print(op1`())
def op3():
    d2 = b2.read()
    e2 = int(d2)
    f2 = c2.read()
    g2 = int(f2)
    return tbh(e2-g2)
#print(op1`())
def op4():
    d3 = b3.read()
    e3 = int(d3)
    f3 = c3.read()
    g3 = int(f3)
    return tbh(e3-g3)
#print(op1())
A=op1()
B=op2()
C=op3()
D=op4()
while True:
    print(A)
    time.sleep(A)
    print(B)
    time.sleep(B)
    print(C)
    time.sleep(C)
    print(D)
    time.sleep(D)

# while True:
#     print(op1())

#print(op1())
# print(op2())
# print(op3())
# print(op4())





# while True:
#     {
#         print(op1())
#         #time.sleep(op1())
#         print(op2())
#         #time.sleep(op2())
#         print(op3())
#         #time.sleep(op3())
#         print(op4())
#         #time.sleep(op4())
#         # firstlane = return op1()
#         # fl =int firstlane
#         # print(fl)
#         # time.sleep(fl)
#         # secondlane = return op2()
#         # sl = int secondlane
#         # print(sl)
#         # time.sleep(sl)
#         # thirdlane = return op3()
#         # tl = int thirdlane
#         # print(tl)
#         # time.sleep(tl)
#         # fourthlane = return op4()
#         # fol = int secondlane
#         # print(fol)
#         # time.sleep(fol)
#
#
#     }

