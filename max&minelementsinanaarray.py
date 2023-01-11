#input : arr[] ={10,20,4}
#output : 20
#output : 4

arr=[1,2,40,3333,3,4,5]

max=arr[0]
n=len(arr)

for i in range(1,n):
    if arr[i]>max:
        max=arr[i]
print(max)

arr=[1,2,40,3333,3,4,5]

min=arr[0]
n=len(arr)
for i in range(1,n):
    if arr[i]<min:
        min=arr[i]
print(min)

