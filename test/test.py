menu = [None, 55, 40, 60]
print('มีเมนู คือ 1:กาแฟ 2:ชาเขียว 3:โกโก้')
selectmenu = int(input("เลือกเมนูที่มี: "))
selectit = menu[selectmenu]
print(f'ราคาของเมนู : {selectit}')
print('-----------------------------------------')
pay = selectit
while pay > 0:
    coin = int(input('กรุณาใส่เหรียญ มีเหรียญ [1,2,5,10]: '))
    if coin in [1, 2, 5, 10]:
        pay -= coin
        if pay > 0:
            print(f'เหลือยอดเงินที่ต้องจ่าย : {pay} บาท')
    else:
        print('ใส่ค่าไม่ถูกต้อง')
change = -pay
if pay == 0:
    print(f'ยอดชำระครบแล้ว ')
elif change > 0:
    print(f'เงินทอนทั้งหมด: {change} บาท')
    a1 = a2 = a3 = a4 = 0
    while change > 0:
        if change >= 10:
            a1 += 1
            change -= 10
        elif change >= 5:
            a2 += 1
            change -= 5
        elif change >= 2:
            a3 += 1
            change -= 2
        elif change >= 1:
            a4 += 1
            change -= 1
        print('----รายการเงินทอน----')
        if a1 > 0:
            print(f'เหรียญ 10 บาท จำนวน: {a1}')
        if a2 > 0:
            print(f'เหรียญ 5 บาท จำนวน: {a2}')
        if a3 > 0:
            print(f'เหรียญ 2 บาท จำนวน: {a3}')
        if a4 > 0:
            print(f'เหรียญ 1 บาท จำนวน: {a4}')
print('------จบการทำงาน-------')
