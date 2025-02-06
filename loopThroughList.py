'''thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
'''

'''thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
  '''
''' 
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1'''

'''thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]'''

'''fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)'''
fruits = ['apple',' orange', 'kiwi', 'mango']
newlist = []
newlist = [x for x in fruits if x != "apple"]
print(newlist)