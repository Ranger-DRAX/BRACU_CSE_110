
#insert
list_1=['apple','banana' ]
list_1.insert(1,'orange')
print(list_1)
#append

#extend
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#extend can use with also tuples,sets , dictionaries
a=['draxx','eat','balls']
b=('ranger','thadoxy' )
a.extend(b)
print(a)
#elements add **instert**
test_list = [['abc','2'],['cds','333'],['efg']]
test_list[2].insert(0,'444')
print(test_list) #output: [['abc', '2'], ['cds', '333'], ['444', 'efg']]
#elements add **
test_list = [['abc','2'],['cds','333'],['efg']]
test_list[2].append('444')
print(test_list)
#output: [['abc', '2'], ['cds', '333'], ['efg', '444']]
#list removes from list
test_list = [['abc','2'],['cds','333'],['efg']]
test_list.pop(2)
print(test_list) #output: '[['abc', '2'], ['cds', '333']]'
#using'del' to remove
test_list = [['abc','2'],['cds','333'],['efg']]
del test_list[0]
print(test_list)
#reverse
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.reverse()
print(fruits)
#remove duplicate values:
t=[7, 7, 7, 1, 0, 3, 3, 55, 9]
rot=[]
for x in t:
    if x not in rot:
        rot.append(x)
print(rot)
#how to take list input without map
t=input().split(',')
u=[]
print(t)
for x in t:
    u.append(int(x))
print(u)
#take list input with map
p=list(map(int,input().split(',')))
#elements swap from list
def swap_position(listx,pos1,pos2):
    listx[pos1],listx[pos2]=listx[pos2],listx[pos1]
    print(listx)
p=[85,98,25,21]
swap_position(p,0,1)
#index method
k=listx.index(2)
#listx.index('Value or elements of list')
#output='index of that value'
###########

