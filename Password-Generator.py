#Password Generator
import random
lst = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],  \
       ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', \
        'k', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
        'z'],\
      ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
      'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
      'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z'],\
      ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']]
s = ['']
numLst = [0, 1, 2, 3]
for i in range(12):
  k = random.choice(numLst)
  s += random.choice(lst[k])
random.shuffle(s)
password = ''
for x in s:
  password += x
print(password)