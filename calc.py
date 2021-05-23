import re
import json
import numpy as np
string = ['Hello world(#*&)', 'images_file']
Mstring=[]
for str in string:
	
	str = str.title()
	str = re.sub('[^A-Za-z0-9]+', '', str)
	

	Mstring.append(str)
	print(str)

print(string)
string = Mstring
print(string)

year = ["2016","2017"]

for y in year:
	print(y)

from random import seed
from random import random
# seed random number generator
seed(1)
num=[]
# generate random numbers between 0-1
for _ in range(10):
	value = random()
	num.append(value)

print(num)

Region ='happ'
Region = Region.upper()

print(Region)
