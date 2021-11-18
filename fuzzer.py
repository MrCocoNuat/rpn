#Generates random commands to fuzz rpn.py
#pipe into rpn.py or output to a file

import sys
import random

keywords = ["+","-","*","/","pop"]
#each of these will remove one element from stack
#each real number will add one element to stack
#attempt to balance these to avoid both a 1M-long stack or an empty one

commandCount = 1000

if len(sys.argv) > 1:
    commandCount = int(sys.argv[1])

#make the first one-hundreth inputs numbers to start the stack off 
for i in range(commandCount):
    print((random.random() if random.getrandbits(1) == 0 or i < commandCount/100 else random.choice(keywords)))
print("stack")
