import time, numpy.random as np, matplotlib.pyplot as plt
def read():
    n=int(input("Enter the number of TV Channels: "))
    return [int(input(f"Enter number of viewers for Channel {i+1}: "))for i in range(n)]
def mergesort(arr):
    if len(arr)>1:
        r=len(arr)//2
        l=arr[:r]; m=arr[r:]
        mergesort(l)
        mergesort(m)
        i=j=k=0
        while i<len(l) and j<len(m):
            (arr[k],i,j,k)=(l[i],i+1,j,k+1) if l[i]<m[j] else (m[j],i,j+1,k+1)
        while i<len(l):
            arr[k],i,k=l[i],i+1,k+1
        while j<len(m):
            arr[k],j,k=m[j],j+1,k+1
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[high],arr[i+1]=arr[i+1],arr[high]
    return i+1
def quicksort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
def selectionsort(arr):
    size=len(arr)
    for step in range(size):
        minidx=step
        for i in range(step+1,size):
            if arr[i]<arr[minidx]:
                minidx=i
        arr[step],arr[minidx]=arr[minidx],arr[step]
def insertionsort(arr):
    for i in range(len(arr)):
        key,j=arr[i],i-1
        while j>=0 and key<arr[j]:
            arr[j+1],j=arr[j],j-1
        arr[j+1]=key
algorithms=[mergesort,quicksort,selectionsort,insertionsort]
labels=["Merge Sort","Quick Sort","Selection Sort","Insertion Sort"]
ch=int(input("1.Merge Sort\n2.Quick Sort\n3.Selection Sort\n4.Insertion Sort\nChoose a method of sorting: "))
method=algorithms[ch-1]
labelData=labels[ch-1]
array=read()
method(array,0,len(array)-1) if ch==2 else method(array)
print(f"Sorted TV Channels in Ascending Order according to number of viewers:\n{array}")
print("Running Time Analysis...")
elements,times=[],[]
for i in range(1,10):
    array=np.randint(0,1000*i,1000*i)
    start=time.time()
    method(array.copy(),0,len(array)-1) if ch==2 else method(array.copy())
    end=time.time()
    print(f"{len(array)} elements sorted by {labelData} in {end-start} seconds!")
    elements.append(len(array))
    times.append(end-start)
plt.xlabel("List Length")
plt.ylabel("Time Complexity")
plt.plot(elements,times,label=labelData)
plt.grid()
plt.legend()
plt.show()