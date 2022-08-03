def str_test(s):
    d = {"upper_case" : 0 ,"lower_case" : 0}
    for x in s :
        if x.isupper():
            d["upper_case"] +=1
        elif x.islower():
            d["lower_case"] +=1
        else:
            pass    
    print("original string:" , s)
    print("no. of upper case characters:", d["upper_case"] )
    print("no. of lower_case:",d["lower_case"])
str_test('The Quick Brown Fox')
