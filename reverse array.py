def reverslist(A,start,end):
    while start < end :
        A[start],A[end]=A[end],A[start]
        start += 1
        end -= 1

A = [1,2,3,4,5]
print(A)
reverslist(A,0,4)
print("reversed array is")
print(A)

