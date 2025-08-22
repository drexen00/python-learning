# Python has no command for declaring a variable.
hello_world = 1 # x is 1, and type is int
hello_world = "Hello World" # x is now "Hello World", not 1, and type is str
print(hello_world)

# casting
x = str(3) # x will be "3" (str), not 3 (int).
x = int(3) # x will be 3 (int), not "3" (str).
x = float(3) # x will be 3.0 (float), not 3 (int).

print(type(x)) # will print <class 'float'>

# you can declare multiple variables at once:
a, y, z = "Orange", "Banana", "Cherry"
print(a) # will print "Orange"
print(y) # will print "Banana"
print(z) # will print "Cherry"

# variables are case-sensitive
b = 4
B = "hello world!" 
print(b) # will print 4
print(B) # will print "hello world!"

# one value to multiple variables
q = w = e = 1
print(q) # will print "1"
print(w) # will print "1"
print(e) # will print "1"

# you can also unpack a list
fruits = ["apple", "banana", "cherry"]
r, t, y = fruits
print(r) # will print "apple"
print(t) # will print "banana"
print(y) # will print "cherry"