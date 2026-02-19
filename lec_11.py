n = [5,3,2,2,1,5,5,7,5,10]
m =[10,111,1,9,5,67,2]
count = 0
for i in range (len(m)):
                    count = 0
                    for j in range (len(n)):
                            if m[i] == n[j]:
                                    count += 1
                    print(count)