# -*- coding: utf-8 -*-
"""adventofcode5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15dz0PJCnbfBIeYANXjZ6xAh3QB-qhD8G
"""

import string

text_file = 'input'
skra = open(text_file, 'r').readlines()
clean = []

for line in skra:
  clean.append(line.replace("\n", ""))

print(skra)
print(clean)
stacks = [['c','q', 'b'], ['z','w','q','r'], ['v','l',',r','m','b'],
          ['w','t','v','h','z','c'], ['g','v','n','b','h','z','d'],
          ['q','v','f','j','c','p','n','h'],
          ['s','z','w','r','t','g','d'], ['p','z','w','b','n','m','g','c'],
          ['p','f','q','w','m','b','j','n']]

def mov(n, starting, ending):
  for i in range(n):
    stacks[ending-1].insert(0, stacks[starting-1][0])
    stacks[starting-1].pop(0)

for line in clean:
  a, n, b, starting, c, ending = line.split()
  mov(int(n), int(starting), int(ending))

for i in range(len(stacks)):
  print(f'stack {i}: ', stacks[i][0])

def mov2 (n, starting, ending):
  temp = []
  for i in range(n):
    temp.append(stacks[starting-1][0])
    stacks[starting-1].pop(0)
  for i in range(len(temp)):
    stacks[ending-1].insert(0,temp[-1])
    temp.pop()

for line in clean:
  a, n, b, starting, c, ending = line.split()
  mov2(int(n), int(starting), int(ending))

for i in range(len(stacks)):
  print(f'stack {i}: ', stacks[i][0])