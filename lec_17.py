
def palendrom (n ,left ,right):
                    
                    if left<=right:
                            if n[left] == n[right]:
                                           return True
                            else:
                                    return False
                    palendrom(n,left+1,right-1)

print(palendrom("kartik",0,5))