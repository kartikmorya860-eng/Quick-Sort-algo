# check palindrom 

n = 12321
num = n
result = 0
while num > 0:
                    last = num % 10
                    result = (result * 10) + last
                    num = num // 10
if n == result:
        print("paindrom")
else:
        print("not")