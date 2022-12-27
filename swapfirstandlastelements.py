#approach1: Tempararory varaiable
mylist=[112,3,4,5,6,7]#6

size= len(mylist)
temp=mylist[0]
mylist[0]=mylist[size-1]
mylist[size-1]=temp
print('approach  1 after swapping',mylist)

#approach2
mylist=[112,3,4,5,6,7]
mylist[0],mylist[-1]=mylist[-1],mylist[0]
print('approach 2 after swapping',mylist)


#approach 3
#using tuple
#get=(7,112)
mylist=[112,3,4,5,6,7]
get=(mylist[-1],mylist[0]) #packing
mylist[0],mylist[-1]=get #unpacking antam anuko
print("after swapping approch 3 ",mylist)

#approach 4
mylist=[112,3,4,5,6,7]
start,*middle,end=mylist
print(start)
print(middle)
print(end)

mylist=[end,*middle,start]

print("after swapping approch 4 ",mylist)

#appraoch 5
mylist=[112,3,4,5,6,7]#index start with 0 remember
first=mylist.pop(0) #112
last=mylist.pop(-1)#7
mylist.insert(0,last)
mylist.append(first)
print("after swapping approch 5 ",mylist)

