#
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#Using Asterisk(*)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)# apple
print(yellow)#banana
print(red) #['cherry', 'strawberry', 'raspberry']
#Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple) #output:('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
#index for tuples
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)
#tuoles count()
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5) #Return the number of times the value 5 appears in the tuple
print(x)
#****dictionary*** $$$'keys':'values'$$$
thisdict={'brand':'ford',"electric": False,'model':'mustang','year':'1946'}
print(thisdict)
print(len(thisdict))
x=thisdict['brand']
d=thisdict.values()
print(d)
m=thisdict.keys()
print(m)
#add items on dictionary
td={"brand": "Ford","model": "Mustang","year": 1964}
td["color"]="red"
print(td)
#remove from dict
td={"brand": "Ford","model": "Mustang","year": 1964}
td.pop('model')
print(td)
#Print all values in the dictionary, one by one:
td={"brand": "Ford","model": "Mustang","year": 1964}
for x in td:
    print(td[x])
##Print all keys in the dictionary, one by one:
td={"brand": "Ford","model": "Mustang","year": 1964}
for x in td:
    print(x)
#Loop through both keys and values, by using the items() method:
td={"brand": "Ford","model": "Mustang","year": 1964}
for x, y in td.items():
    print(x,y)
#take input for dictionary
#a
n=int(input())
d={}
for x in range(n):
    a=input()
    b=input()
    d.update({a:b})
print(d)
#b
n=int(input())
d={}
for x in range(n):
    a=input()#keys
    b=input()#values
    d[a]=b
print(d)
#another input method of dictionary by comma
a=input().split(',')
d={}
for x in a:
    d.update({x.split(':')[0].strip():x.split(':')[-1].strip()})
print(d)
