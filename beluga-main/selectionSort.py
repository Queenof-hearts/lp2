def selectionSort(arr,size):
    for i in range(size):
        min_index=i
        for j in range(i+1,size):
            if arr[j]<arr[min_index]:
                min_index=j
        (arr[i],arr[min_index])=(arr[min_index],arr[i])
 
arr=[]
n=int(input("enter no. of elements in array: "))
for i in range(n):
    num=int(input(f"enter element {i+1}: "))
    arr.append(num)
print(arr)
selectionSort(arr,n)
print("after sorting: ")
print(arr)