def reverseInParentheses(inputString):
    paren_closure = start_end(inputString)
    list1 = list(inputString)

    for elements, values in paren_closure.items():
        list1[elements:values] = reversed(list1[elements:values])

    unwanted_elements = {'(', ')'}
    list2 = [ele for ele in list1 if ele not in unwanted_elements]
    final_merge = "".join(list2)
    return final_merge

def start_end(inputString):
    istart = []  # stack of indices of opening parentheses
    d = {}
    for i, c in enumerate(inputString):
        if c == '(':
            istart.append(i)
        if c == ')':
            try:
                # # d[7] = 8, d[9] = 10 and d[4] = 14
                # pop the last number add it as a key, value for the key is the value of i
                d[istart.pop()] = i
            except IndexError:
                print('Too many closing parentheses')
    if istart:  # check if stack is empty afterwards
        print('Too many opening parentheses')
    return d
inputString = "foo(bar(baz))blim"
# Because "foo(bar(baz))blim"
# becomes "foo(barzab)blim"
# and then "foobazrabblim"
# inputString = "foo(bar)baz(blim)"

print(start_end(inputString))

print(reverseInParentheses(inputString))

# another solution
def reverseInParentheses(s):
    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')
# inputString = "foo(bar(baz))blim"
# Because "foo(bar(baz))blim"
# becomes "foo(barzab)blim"
# and then "foobazrabblim"
inputString = "foo(bar)baz(blim)"

reverseInParentheses(inputString)