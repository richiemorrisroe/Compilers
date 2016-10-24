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
while(True):
    expr = raw_input("What mathematical operation would you like me to perform?")
    res = eval(expr)
    print(res)
    print("The answer is: {res}".format(res=res))
