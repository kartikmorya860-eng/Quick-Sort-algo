n = int(input("Enter the number :"))
num = n
total = 0
node = len(str(num))
while num > 0:
                    last = num % 10
                    num = num // 10
                    total  = last**node + total
if total == n:
                    print("armstrong")
else:
                    print("not")