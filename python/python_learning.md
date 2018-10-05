# Documentation:

```py
# Printing documentation in console, e.g. docs on 'str' function
print(help(str))
```

# String Formatting:

```py
greeeting = 'Hello'
name = 'Michael'

# Format using curly brackets
message = '{}, {}. Welcome!'.format(greeting, name)

# Format using f-strings
message = f'{greeting}, {name.upper()}. Welcome!'
```

# Number Functions:

```py
# Return absolute value (i.e. positive value) of a number
abs(-3.134)     # returns 3.134

```

# Lists:

## Slicing:
```py
message = 'hello world'
print(message[-4])  # returns 'o'
print(message[2:5]) #returns 'llo'
```
## Functions:

## Append
```py
some_list.append('foo')
```

## Insert a single value
```py
some_list.insert(0, 'foo')

#e.g2: insert a list into a single index:
some_list.insert(0, another_list)
```

## Extend a list with multiple values
```py
another_list = ['foo', 'bar']
some_list.extend(0, another_list)
```

## Remove Values:
```py
some_list.remove()
some_list.pop()
```

## Other functions:
```py
some_list.reverse
some_list.sort      # sorts list in-place
sorted(some_list)   # returns sorted list, rather than sorting in-place
min(some_list)
max(some_list)

'foo' in some_list  # returns boolean if 'foo' exists in list
```

# Enumerate

```py
courses = ['History', 'Maths', 'Physics', 'CompSci']
some_list = []

# e.g1:
for course in enumerate(courses):
    print(course)
# prints (0, 'History'), (1, 'Maths'), (2, 'Physics'), (3, 'CompSci')

# e.g2:
for index, course in enumerate(courses, start=1):
    some_list.append(course)

# prints: 1 History 2 Maths 3 Physics 4 CompSci
```

# eval and exec
- exec can execute a string expression block of python code
- eval is used to evaluate a single dynamically generated Python expression
```py
#e.g1: execute a string statement using exec:
expression = 'if 2 == 2: print("bob")'
exec(expression)
-> bob

#e.g2: evaluate a dynamic string expression
a,b = 3,4
eval('3+4')
-> 7

expression = 'print(2+5)'
eval(expression)

```

# Comprehensions
## List Comprehension
- Easier and more readable way of creating lists

```py
# eg.1: a simple converstion:

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## using for-loops
my_list = []
for n in nums:
    my_list.append(n)
-> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## using list comprehensions
my_list = [n for n in nums]
-> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# eg.2: squared values (can also be done using map&lambda):
my_list = [n*n for n in nums]
-> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# eg.3: only even numbers (can also be done using filter&lambda)
my_list = [n for n in nums if n%2 == 0]
-> [2,4,6,8,10]


# eg.4 print letters a,b,c,d with every combination of 1,2,3,4:

## using for-loop:
my_list = []
for letter in 'abcd':
    for num in range(4)
        my_list.append((letter,num))
-> [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0)...('d', 3)]

## using list comprehensions
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
-> [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0)...('d', 3)]

```

## Dictionary Comprehension

```py
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# eg.1: Create a dictionary of names corresponding to their heroes (e.g. {'Bruce': 'Batman'} )

## Using for-loop
my_dict = {}
for name, hero in zip(names, heroes):
    my_dict[name] = hero



## using dictionary comprehensions
{name : hero for name,hero in zip(names, heroes)}
-> {'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}
```

## Set Comprehension

- note: sets a create using {} brackets, e.g. {1,2,3,4,5,5,5} -> {1,2,3,4,5}


```py
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
# eg.1: create a set with only unique values from nums

## using for-loop
my_set = set()
for n in nums:
    my_set.add(n)
-> {1, 2, 3, 4, 5, 6, 7, 8, 9}


## using set comprehension:
{n for n in nums}
-> {1, 2, 3, 4, 5, 6, 7, 8, 9}
```


## Creating Generators using list comprehensions:

```py
nums = [1,2,3,4,5,6,7,8,9]
# eg.1: create a generator function which generates squares of each num

## using generator function

def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)

for i in my_gen:
    print (i)

-> 1, 4, 9, 16, 25, 36, 49, 64, 81


## using list comprehension

# NOTE: the list comprehension is created using () brackets for generators (instead of [])

my_gen = (n*n for n in nums)
for i in my_gen:
    print (i)
-> 1, 4, 9, 16, 25, 36, 49, 64, 81
```

# MAP / REDUCE / LAMBDA / REDUCE ??