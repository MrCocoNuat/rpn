stack = []

done = False

helpText = '''
The prompt is "[n]$", where n is the stack height

The allowed user keywords are:

<any real number> : push that number to stack

"stack"           : print whole stack
"pop"             : remove top element
"clear"           : erase stack

These binary operators remove the top two elements and push the result
["add","+"]       : binary addition
["subtract","-"]  : binary subtraction, top element is the subtrahend
["multiply","*"]  : binary multiplication
["divide","/"]    : binary division, top element is the denominator

currently this calculator ignores any divisions by 0 with a warning

These keywords cause the program to ignore everything after them
"help"            : print this help message
"exit"            : exit program
EOF               : exit program

Any number of keywords may be input at once, separated by single spaces
after each entry the top of the stack is printed for convenience
'''

welcome = '''
Simple RPN calculator, type "help" for help
'''
print(welcome)

done = False

while not done:
    print("[{n}]$ ".format(n=len(stack)),end="")
    try :
        args = input().split(" ")
    except EOFError:
        print()
        exit()
        
    for a in args:
        isNumeric = True
        try:
            a = int(a)
        except:
            try:
                a = float(a)
            except:
                isNumeric = False

        if isNumeric:
            stack.append(a)
        else:

            if a == "exit":
                exit()
            if a == "help":
                print(helpText)
                break
            if a == "stack":
                for s in stack[:-1]:
                    print(s)
            elif a == "clear":
                stack = []
            elif a == "pop":
                if len(stack) > 0:
                    stack = stack[:-1]
            elif a == "add" or a == "+":
                if len(stack) > 1:
                    stack[-2] += stack[-1]
                    stack = stack[:-1]
            elif a == "subtract" or a == "-":
                if len(stack) > 1:
                    stack[-2] -= stack[-1]
                    stack = stack[:-1]
            elif a == "multiply" or a == "*":
                if len(stack) > 1:
                    stack[-2] *= stack[-1]
                    stack = stack[:-1]
            elif a == "divide" or a == "/":
                if len(stack) > 1:
                    if stack[-1] == 0:
                        print("Attempted to divide by 0")
                    else:
                        stack[-2] /= stack[-1]
                        if stack[-2] == int(stack[-2]):
                            stack[-2] = int(stack[-2])
                        stack = stack[:-1]

    if len(stack) > 0:
        print(stack[-1])
    else:
        print("empty")
                
        
