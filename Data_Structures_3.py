##% Conditional are made up of if's and else's
x = 2
if x % 2 == 0:
  print('x is even.')
else:
  print('x is odd')

##% "elif" (else if) is used to go through multiple conditions
if x % 3 == 0:
  print('x is divisible by 3.')
elif x % 3 == 1:
  print('x is congruent to 1 mod 3.')
else:
  print('x is congruent to 2 mod 3.')

##% "and" and "or" are used to check for the truth value of combined conditions
if x > 0 and x % 2 == 0:
  print('x is a positive even integer')

if x % 2 == 0 or x % 3 == 0:
  print('x is divisible by either 2 or 3.')

##% Conditionals can be nesting inside each other.
if x % 2 == 0:
  if x % 3 == 0:
    print('x is divisible by 6')
  else: print ('x is divisible by 2 but not by 3')

##% While loops check for the condition at each step.
x = 1
while x < 10:
  print(x)
  x += 1

print('Loop finished.')

##% For loops are used to iterate through a sequence of elements.
a = [1, 2, 3]
for item in a:
  print(item)

print()

##% range(n) returns an iterator from 0 to n-1
for index in range(len(a)):
  print(index, a[index])

##% One can loop through the keys in a dictionary in a for loop
dict = {'a': 1, 'b': 2, 'c': 3}
for key in dict:
  print(key, dict[key])

##% enumerate() returns the invidual elements and their corresponding index
# in pairs in a lists
for index, value in enumerate(a):
  print(index, value)

##% zip() returns the individual elements of two given lists in pairs
b = [2, 3, 4]
print(a)
print(b)
print()

for a_i, b_i in zip(a, b):
  print(a_i, b_i)