import string as s
def make_comparator(list):
    def comp(char):
        if char in list:
            return char
        else:
            pass
        return(comp)

is_number = make_comparator(s.digits)
# is_letter= make_comparator(s.ascii_letters)
# mult_ops = ['*', '/']
add_ops = ['+', '-' ]
brackets = ['(', ')']
is_add_op=make_comparator(add_ops)
# is_mult_op=make_comparator(mult_ops)
is_bracket=make_comparator(brackets)
# is_whitespace = make_comparator(s.whitespace)
# assigns = [':', '=']
# is_equal = make_comparator(assigns[1])
# is_colon = make_comparator(':')
# is_dot = make_comparator('.')
# print("made around {d} objects".format(d=len(dir())))
# var = raw_input("Give a function: ")
# print("You entered {v}".format(v=var))
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
    expr = raw_input("What mathematical operation would you like me to perform?")
    nums = []
    ops = []
    
    for each in expr:
        if is_number(each):
            nums.append(each)
        if is_add_op(each):
            ops.append(each)
            #leave this out first
        # if is_bracket(each):
        for num, op in nums, ops:
            res = 0
            if(ops=="+"):
                res = plus(num, y)
                
            eval()
    print(res)
    print("The answer is: {res}".format(res=res))
