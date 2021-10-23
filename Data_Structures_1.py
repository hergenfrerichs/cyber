print("Hello World!")
##% A Python list is an array of ordered elements.
a = [1, 2, 3]
print(a[0])
print(a[2])
print(a[-2])
##% Slicing a Python list results in a sublist.
b= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(b)
print(b[1:5])
##% Skipping can be done with a second colon
print(b[1::2])
##% A list can be extended via appending or concatenation.
c=[1, 2, 3]
print(c)
c.append(4)
print(c)
c = c + [5, 6, 7]
print(c)
##% len() returns the length of a list
print(len(c))
##% Tuples are very similar to lists.
a=(2, 1, 2)
print(a[1])
print(a[1:3])
print(len(a))
##% Tuples cannot be mutated.
a[0] = 0
##% A dictionary is initialized with curly braces
a = {'Alice': 2,'Bob': 5,'Carol': 10}
print(a['Alice'])
print(a['Carol'])
print(a['Dan'])
##% Adding a new key is done in the same way as changing the value of a key.
a['Bob'] = 7
a['Dan'] = 6
print(a)
##% Not everything can be a dictionary key.
a[1] = 2
a[(1, 2)] = 0
a[[1, 2]] = 0
print(a)
##% A Python set can be declared with curly braces.
a = {1, 2, 3}
##% Items that are already in a set won't be added again.
a.add(4)
print(a)
a.add(3)
print(a)
##% Unions and intersections of sets can be computed.
b = {2, 4, 5}
print('A intersect B:')
print(a.intersection(b))
print('B union A:')
print(b.union(a))
##% Functions

def foo(name):
  print('Hello from', name,'!')

def bar():
  return 1

foo('Quan')
x = bar()
print(x)
