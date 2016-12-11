import string as s
def make_comparator(list):
    def comp(char):
        if char in list:
            return char
        else:
            pass
        return(comp)

def is_add_op(char):
    if char in '+-':
        return char
    else:
        pass
is_number = make_comparator(s.digits)
##start with simple calculator language
##implement plus, minus and parentheses
def plus(x, y):
    x + y
def minus(x, y):
    x - y
def multiply(x, y):
    x*y
def divide(x, y):
    x/y
while(True):
    expr = input("What mathematical operation would you like me to perform?")
    nums = []
    ops = []
    expr.split()
    print(expr)
    for each in expr:
        print(type(each))
        if is_number(each):
            nums.append(each)
        # if is_add_op(each):
        #     ops.append(each)
            #leave this out first
        # if is_bracket(each):
        # for num, op in nums, ops:
        #     res = 0
        #     if(ops=="+"):
        #         res = plus(num, y)
    print("The operators are: {ops}".format(ops=ops))
    print("The numbers are: {nums}".format(nums=nums))
