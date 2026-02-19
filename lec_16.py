# arr=[1,2,3,4,5,6,7,8,9]
# left,right  =1,5
# def reverseArray(arr, left, right):
#     if left >= right:
#         return
    
#     arr[left], arr[right] = arr[right], arr[left]
#     reverseArray(arr, left + 1, right - 1)
#     return arr
# print(reverseArray(arr,left ,right))



def arrpalendrom(arr, left, right):
    if left >= right:
        print("The sequence is a palindrome")
        return True
    if arr[left] != arr[right]:
        print("The sequence is not a palindrome")
        return False
    return arrpalendrom(arr, left + 1, right - 1)

n = int(input().strip())
arr = list(map(int, input().split()))
print(arrpalendrom(arr, 0, n - 1))