#appraoch 1
mylist=[12,2,44,67,77]
print(mylist)
pos1,pos2=1,3
mylist[pos1],mylist[pos2]=mylist[pos2],mylist[pos1]
print('after swapping',mylist)

#approach2
mylist=[12,2,44,67,77]
print(mylist)
pos1,pos2=1,3
first_ele=mylist.pop(pos1)
sec_ele=mylist.pop(pos2-1)
mylist.insert(pos1,sec_ele)
mylist.insert(pos2,first_ele)
print(mylist)
