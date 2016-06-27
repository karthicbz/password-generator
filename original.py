from values import capital_alpha
from values import small_alpha
from values import numbers
from values import special
import random

def capital(x):#This unction will produce values for capital letter
    x = capital_alpha
    ckey = []
    ckey1 = []
    for key in x:
        ckey.append(key)
    for i in range(0, strength):
        ckey1.append(random.choice(ckey))
    return ckey1

def small(y):#This function will produce values for small letter
    y = small_alpha
    skey = []
    skey1 = []
    for key in y:
        skey.append(key)
    for i in range (0, strength):
        skey1.append(random.choice(skey))
    return skey1

def numb(n):#This function will produce the values for numbers
    n = numbers
    n1 = []
    for i in range(0, strength):
        n1.append(random.choice(n))
    return n1

def speci(s):#This function will produce the values for special character
    s = special
    s1 = []
    for i in range(0, strength):
        s1.append(random.choice(s))
    return s1
print "Welcome to password generator"
print "You can get a unhackable passwords here"
print "select one to get your password"
print "1-->Weak"
print "2-->Intermediate"
print "3-->strong"
inp = input("Your Input:")
if inp == 1:
    strength = input("Enter your strength between 6 - 12:")
    while strength < 6 or strength > 12:
        strength = input("Please enter the range between 6 - 12:")
elif inp == 2:
    strength = input("Enter your strength between 13 - 24:")
    while strength < 13 or strength > 24:
        strength = input("Please enter the range between 13 - 24:")
elif inp == 3:
    strength = input("Enter your strength between 24 - 48:")
    while strength < 24 or strength > 48:
        strength = input("Please enter the range between 24 - 48:")
else:
    if inp == 0 or inp > 3:
        strength = 0
        
#print capital(strength)
#print small(strength)
#print numb(strength)
#print speci(strength)
k = small('y') + capital('x') + numb('n') + speci('s')#Joining all the values of functions together
final = []
if strength == 0:#if strength is 0 print this
    print "Wrong Input"
    print "Nothing Generated"
else:#if print is a value other than '0' print this
    for i in range(0, strength):
        final.append(random.choice(k))#Again appending and joining values into final list
    string = ''.join(str(e) for e in final)
    print "Hola! Password Generated:", string

'''def cap_small(c, sm, nu, sp):#Using both capital and small dictionaries
    c = capital_alpha
    sm = small_alpha
    nu = numbers
    sp = special
    equals = []
    for i in final:
        for key in c:
            if i == key:
                equals.append(capital_alpha[i])
            
            #elif i == key:
                #equals.append(small_alpha[i])
    return equals
print cap_small('c', 'sm', 'nu', 'sp')'''
