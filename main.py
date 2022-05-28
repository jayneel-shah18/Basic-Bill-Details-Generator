import random

def gen_OID():
    r = random.randrange(0,999999)
    r = str(r)
    r = r.rjust(6,'0')
    r = 'O' + r
    return r

print("Welcome to the Restaurant!")
name = input("Please Enter Your Name: ")
mno = input("Please Enter Your Contact Number: ")
assert len(mno) == 10, "Contact Number should be of 10 digits"
menu = {"1) Masala Dosa":50, "2) Idli Sambhar":30, "3) Vada Sambhar":30, "4) Sada Dosa": 25, "5) Mysore Masala Dosa":60, 
        "6) Spring Dosa":70, "7) Filter Coffee": 35, "8) Extra Chutney": 5, "9) Extra Sambhar": 15, "10) Extra Idli": 10}

print("Menu Card")
for x,y in menu.items():
    print(x,':',y)

no = int(input("How many items would you like to order?: "))
order = {}

for i in range(no):
    print("Enter item number followed by quantity.")
    keys = int(input()) 
    assert keys >= 1 and keys <= 10, "Wrong Item Number!"
    values = int(input())
    assert values > 0, "Quantity has to be positive!"
    
    if keys in order.keys():
        order[keys] += values
    else:
        order[keys] = values

total = []
t = 0
for x,y in order.items():
    if x == 1:
        total.append(50*y)
    elif x == 2:
        total.append(30*y)
    elif x == 3:
        total.append(30*y)
    elif x == 4:
        total.append(25*y)
    elif x == 5:
        total.append(60*y)
    elif x == 6:
        total.append(70*y)
    elif x == 7:
        total.append(35*y)
    elif x == 8:
        total.append(5*y)
    elif x == 9:
        total.append(15*y)
    elif x == 10:
        total.append(10*y)

for i in total:
    t = t + i
print("-"*70)
print(gen_OID())
print("-"*70)
print("Bill")
print("Name: {}   Contact Number: {}".format(name,mno))
print("-"*70)
print("Item\t\t\tQuantity\t\t\tTotal")
print("-"*70)
for x,y,z in zip(order.keys(),order.values(),total):
        if x == 1:
            print("Masala Dosa\t\t\t{}\t\t\t{}".format(y,z))
        elif x == 2:
            print("Idli Sambhar\t\t\t{}\t\t\t{}".format(y,z))
        elif x == 3:
            print("Vada Sambhar\t\t\t{}\t\t\t{}".format(y,z))
        elif x == 4:
            print("Sada Dosa\t\t\t{}\t\t\t{}".format(y,z))
        elif x == 5:
            print("Mysore Masala Dosa\t\t{}\t\t\t{}".format(y,z))
        elif x == 6:
            print("Spring Dosa\t\t\t{}\t\t\t{}".format(y,z))
        elif x == 7:
            print("Filter Coffee\t\t\t{}\t\t\t{}".format(y,z))
        elif x == 8:
            print("Extra Chutney\t\t\t{}\t\t\t{}".format(y,z))
        elif x == 9:
            print("Extra Sambhar\t\t\t{}\t\t\t{}".format(y,z))
        elif x == 10:
            print("Extra Idli\t\t\t{}\t\t\t{}".format(y,z))
print("-"*70)
print("\t\t\tGrand Total\t\t\t{}".format(t))
print("-"*70)
