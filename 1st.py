rand_string = "  this is an             "
rand_string = rand_string.lstrip()
print(rand_string)
print(rand_string.upper())

import os
print os.getcwd()
print("Hello world")
print("tis lin")
inputs = 9
while inputs != 0:
    inputs = input("enter ")
    print(inputs)
    if inputs == 3:
        print("it is 3")
    else:
        print("It is not 3")

from PIL import Image
ba = Image.open('naver.jpg')
ba.show();
