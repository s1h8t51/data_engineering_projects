msg1 = 'Fred scored {} out of {} points.'
msg1.format(3, 10)
# => 'Fred scored 3 out of 10 points.'

msg2 = 'Fred {verb} a {adjective} {noun}.'
msg2.format(adjective='fluffy', verb='tickled', noun='hamster')
# => 'Fred tickled a fluffy hamster.'

greeting = "Welcome To Chili's"

print(greeting.lower())
print(greeting.upper())
# Prints: welcome to chili's

text1 = '   apples and oranges   '
text1.strip()       # => 'apples and oranges'

text2 = '...+...lemons and limes...-...'

# Here we strip just the "." characters
text2.strip('.')    # => '+...lemons and limes...-'

# Here we strip both "." and "+" characters
text2.strip('.+')   # => 'lemons and limes...-'

# Here we strip ".", "+", and "-" characters
text2.strip('.+-')  # => 'lemons and limes'

my_var = "dark knight"
print(my_var.title()) 

# Prints: Dark Knight


text = "Silicon Valley"

print(text.split())     
# Prints: ['Silicon', 'Valley']

print(text.split('i'))  
# Prints: ['S', 'l', 'con Valley']

mountain_name = "Mount Kilimanjaro"
print(mountain_name.find("o")) # Prints 1 in the console.

fruit = "Strawberry"
print(fruit.replace('r', 'R'))

# StRawbeRRy



x = "-".join(["Codecademy", "is", "awesome"])

print(x) 
# Prints: Codecademy-is-awesome


txt = "She said \"Never let go\"."
print(txt) # She said "Never let go".


game = "Popular Nintendo Game: Mario Kart"

print("l" in game) # Prints: True
print("x" in game) # Prints: False


str = 'yellow'
str[1]     # => 'e'
str[-1]    # => 'w'
str[4:6]   # => 'ow'
str[:4]    # => 'yell'
str[-3:]   # => 'low'


str = "hello"
for c in str:
  print(c)
  
# h
# e
# l
# l
# o


length = len("Hello")
print(length)
# Output: 5

colors = ['red', 'yellow', 'green']
print(len(colors))
# Output: 3

x = 'One fish, '
y = 'two fish.'

z = x + y

print(z)
# Output: One fish, two fish.

x = 'One fish, '
y = 'two fish.'

z = x + y

print(z)
# Output: One fish, two fish.