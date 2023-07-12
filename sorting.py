import time
from numpy.random import randint
import matplotlib.pyplot as plt
#Mergesort in python
def mergeSort(array):
    if len(array) > 1:
        r = len(array)//2
        L=array[:r]
        M=array[r:]
        mergeSort(L)
        mergeSort(M)

        i=j=k=0

        while i<len(L) and j<len(M):
            if L[i]<M[j]:
                array[k]=L[i]
                i+=1
            else:
                array[k]=M[j]
                j+=1
            k+=1
        while i<len(L):
            array[k] = L[i]
            i+= 1
            k+=1
        while j<len(M):
            array[k] = M[j]
            j += 1
            k +=1
#quicksort in pytgon
def partition(arr,low,high):
    i=(low-1)
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return(i+1)
def quickSort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)
#Selection Sort
def selectionSort(array,size):
    for i in range(size):
        min=i
        for j in range(i+1,size):
            if(array[j]<array[min]):
                min = j
        array[i],array[min]=array[min],array[i]
def read_Input():
    a=[]
    n=int(input("Enter the number of TV channels"))
    print("Enter the number of viewers")
    for i in range(0, n):
        l=int(input())
        a.append(l)
    return a
elements = list()
times = list()
global labeldata
print("1.Merge sort 2.Quick sort 3.Selection Sort")
ch = int(input("Enter the choice"))
if(ch==1):
    array=read_Input()
    mergeSort(array)
    labeldata="MergeSort"
    print('Sorted Array is:')
    print(array)
elif (ch==2):
    array=read_Input()
    size=len(array)
    labeldata="QuickSort"
    quickSort(array,0,size-1)
    print("sorted array is:")
    print(array)
if (ch==3):
    array=read_Input()
    size=len(array)
    labeldata="SelectionSort"
    selectionSort(array,size)
    print('Sorted Array is:')
    print(array)
print("************************Run Time Analysis******************************")
for i in range(1,10):
    array=randint(0,1000*i,1000*i)
    start=time.time()
    if ch==1:
        mergeSort(array)
    elif ch==2:
        size = len(array)
        quickSort(array,0,size-1)
    else:
        size=len(array)
        selectionSort(array,size)
    end=time.time()
    print(len(array),"Elements Sorted by",labeldata,end-start)
    elements.append(len(array))
    times.append(end-start)
plt.xlabel("List Length")
plt.ylabel("Time Complexity")
plt.plot(elements,times,label=labeldata)
plt.grid()
plt.legend()
plt.show()