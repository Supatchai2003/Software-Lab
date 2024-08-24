menu = [None,51,42,27]
print("################Menu################\n ####  1.Coffee 2.Coco 3.Tea  ####\n####################################")
selectmenu = int(input("CHOOSE MENU : [1-3]"))
selectit = menu[selectmenu]
print(f"Cost = {selectit}")
print("####################################")
pay = selectit
while pay > 0:
    coininsert = int(input("please insert coin : [1,2,5,10]"))
    if coininsert == 1 or coininsert == 2 or coininsert == 5 or coininsert == 10:
        if pay > 0 :
            pay = pay - coininsert
            print(f"please insert: = {pay}")
    else:
        print("invalid value")
change = -pay
print(f"change {change}")
amount1 = 0
amount2 = 0
amount3 = 0
amount4 = 0
while change > 0:
    if change >= 10:
        print("##########chage money###########")
        change = change - 10
        amount1 = amount1 + 1
        if amount1 > 1:
            print(f"change : 10  Amount : {amount1}")
        else:
            print(f"change : 10  Amount : 1")
    elif change <= 9 and change > 4:
        print("##########chage money###########")
        change = change - 5
        amount2 = amount2 + 1
        if amount2 > 1:
            print(f"change : 5  Amount : {amount2}")
        else:
            print(f"change : 5  Amount : 1")
    elif change <= 4 and change >=2:
        print("##########chage money###########")
        change = change - 2
        amount3 = amount3 + 1
        if amount3 > 1:
            print(f"change : 2  Amount : {amount3}")
        else:
            print(f"change : 2  Amount : 1")
    elif change <= 1 and change > 0:
        print("##########chage money###########")
        change = change - 1
        amount4 = amount4 + 1
        if amount4 > 1:
            print("##########chage money###########")
            print(f"change : 1  Amount : {amount4}")
        else:
            print(f"change : 1  Amount : 1")
print("################END#################")