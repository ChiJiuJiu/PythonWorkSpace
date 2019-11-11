A=[2,1,13,3,16,4,11,24,5,7,12,15]


def  parttion(v,left,right):
    key=v[left]
    start,end=left,right
    while start<end:
        while start<end  and v[end]>key:
            end-=1
        v[start]=v[end]
        while start<end  and v[start]<key:
            start+=1
        v[end]=v[start]
    v[start]=key
    return  start

def  quick_sort(v,left,right):
    if left>=right:
        return
    p=parttion(v,left,right)
    quick_sort(v,left,p-1)
    quick_sort(v,p+1,right)

if __name__ == '__main__':
    quick_sort(A,0,len(A)-1)
    print(A)
