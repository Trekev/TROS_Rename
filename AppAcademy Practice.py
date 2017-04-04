import numpy as np

def lucky_sevens(numbers):

    for i in np.arange(len(numbers)-1):
            if sum(numbers[(0+i):(3+i)]) == 7:
                if (3+i) > (len(numbers)):
                    break
                else:
                    return True

    return False

#print(lucky_sevens([0,-2,1,8]))

def oddball_sum(numbers):
    a = []
    for i in numbers:
        if i % 2 != 0:
            a.append(i)
    print(a)
    return(sum(a))

def disemvowel(string):
    vowel = ['a','e','i','o','u']
    stringSplit = list(string)

    for i in vowel:
        while i in stringSplit:
            stringSplit.remove(i)
    string = ''.join(stringSplit)
    return string

disemvowel("foobar")