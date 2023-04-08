"""
x = input()

y=len(x)
if(y<=3):
    print(x)
elif(x[-3:]=="ing"):
    print(x + "ly")
else:
    print(x + "ing")
"""
def add_string(str):

    length = len(str)
    if(length>2):
        if(str[-3:]=="ing"):
            return str+"ly"
        else:
            return str+"ing"
    return str

print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))