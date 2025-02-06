'''thistuple = ("apple", "banana", "cherry")
print(thistuple)'''
'''
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)'''
'''
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])'''

'''thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
'''

'''x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)'''

'''thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)'''


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
