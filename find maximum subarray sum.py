# to find maximum subarray sum


def maxsubarrsum(a):
    m=a[0]
    s=0
    
    for i in range(len(a)):
        m = m + arr[i]
        if m < 0:
            m = 0
        
        
        elif (s < m):
            s = m
            
    return s

arr = [-1,2,3,4,1,-10, 80]
print(maxsubarrsum(arr))
