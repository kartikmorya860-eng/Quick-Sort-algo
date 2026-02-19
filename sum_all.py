# import array 
# arr = array.array('i', [1, 2, 3, 4, 5])
# for i in range(0,len(arr)):
#                     for j in range(arr[i],-1,-1):
#                         print(arr[j])



# arr = array.array('i', [0, 2, 0, 4, 5, 0, 0, 5, 6])
# for i in range (0,len(arr)):
#                     for j in range (1,len(arr)):
#                             if (arr[i] != 0):
#                                     swap(arr[i],arr[j])
#                                     i += i
#                                     print(arr[i])


# arr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# sum = 0
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if (i == j):
#             sum += arr[i][j]
#         print(sum)


n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
for i in range(len(m)):
    count = 0
    for j in range(len(n)):
        if m[i] == n[j]:
            count += 1
    print(count)