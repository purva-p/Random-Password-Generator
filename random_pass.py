import random

upper_char =['A','B','C','D','E']
lower_char =['a','b','c','d','e']
num=['1','2','3','4','5']
special_char=['@','#','^','&','!']

passw = random.choice(upper_char) + random.choice(lower_char) + random.choice(num) + random.choice(special_char)

print(passw)