import string as s


def make_comparator(l):
    print(l)

    def comp(char):
        print(char)
        if char in l:
            return char
        else:
            pass
        return comp


def is_add_op(char):
    if char in "+-":
        return char
    else:
        pass


is_number = make_comparator(s.digits)

# start with simple calculator language
# implement plus, minus and parentheses


def plus(x, y):
    x + y


def minus(x, y):
    x - y


def multiply(x, y):
    x * y


def divide(x, y):
    x / y


operators = "+-"

while True:
    expr = input("What mathematical operation would you like me to perform?")
    nums = []
    ops = []
    fullexp = []
    expr.split()
    print(expr)
    for element in expr:
        fullexp.append(element)
        if element in s.digits:
            nums.append(element)
        if element in operators:
            ops.append(element)
        else:
            pass
        # leave this out first
        # if is_bracket(each):
        # for num, op in nums, ops:
        #     res = 0
        #     if(ops=="+"):
        #         res = plus(num, y)
    print("The operators are: {ops}".format(ops=ops))
    print("The numbers are: {nums}".format(nums=nums))
