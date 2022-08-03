a = input("enter a string: ")#option 1 for entering user input.
def reverse(a):
    b = " "
    for i in range (len(a)):
        b = a[i] + b
    return (b)
#a = input("enter a string: ")#option 2 for entering user input.
print (reverse(a))


