'''def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")'''

'''def my_function(*malyshy):
  print("The youngest child is " + malyshy[2])

my_function("Emil", "Tobias", "Linus")'''

'''def my_function(country="Kazakhstan"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)'''

'''def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))'''

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)